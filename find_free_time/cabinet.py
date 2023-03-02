from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Save_pickle_file.save_data import save_data_pickle
from must_have.crome_options import setting_chrome_options
from must_have.credentials import get_credentials
from must_have.soup import get_soup
import time
from doctor_and_specialization import find_specialization
from xlsx_tools.create_XLXS_report_file import create_report


def select_specialization(specialization_index):
    Select(WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "POPUP_SPECIALIZATION")))).select_by_value(specialization_index)


def select_doctor(doctor_index):
    doctor = Select(WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "body > main > section > form > "
                                    "fieldset.appointment-online__form-fieldset.--col-2.step4 >"
                                    " label > div > select"))))

    time.sleep(5)
    doctor.select_by_value(doctor_index)


def get_information_from_page(page_html):  # receive information from page fo activ day for selected doctor
    soup = get_soup(page_html)
    month = soup.find('div', class_='datepicker-days').find(class_="datepicker-switch").text  # current month
    active_day = soup.find('div', class_='datepicker-days').find(class_="active day").text  # activ (selected) day
    all_days = soup.find('div', class_='datepicker-days').find_all(class_="day")  # all days
    doctor_family_name = soup.find(class_="fio").text  # doctor family
    address = soup.find(class_='data__item data__item__address').text  # clinick adress
    active_day_time = soup.find(class_="spanSelectors").find_all('span', class_="time")  # active day appointments
    return month, active_day, active_day_time, address, doctor_family_name, all_days


def select_day_from_list(day_number):
    day = browser.find_element(By.CLASS_NAME, 'table-condensed').find_element(By.TAG_NAME, 'tbody') \
        .find_element(By.XPATH, f"//td[(text()={day_number}) and not(contains(@class, 'disabled'))]")
    day.is_selected()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable(day))
    day.click()


def appointment_date_and_time(active_day_time, all_days):
    time_in_active_day_list = [x.text for x in active_day_time]
    aviable_days_list = [day.text for day in all_days if 'disabled' not in day.get('class')]
    return aviable_days_list, time_in_active_day_list


def select_clinic():
    browser.find_element(By.XPATH, '/html/body/main/section/form/fieldset[9]/label[2]/span').click()  # select clinic
    return browser.page_source


def enter_cabinet():
    login, password = get_credentials()

    browser.get('https://clinic-complex.ru/cabinet/')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "USER_LOGIN_POPUP")))

    search_input = browser.find_element(By.ID, "USER_LOGIN_POPUP")
    search_input.clear()
    search_input.send_keys(login)

    search_input = browser.find_element(By.ID, "USER_PASSWORD_POPUP")
    search_input.clear()
    search_input.send_keys(password)
    browser.find_element(By.NAME, 'Login').click()

    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "--online-order")))
    browser.find_element(By.CLASS_NAME, "--online-order").click()
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "appointment-online__form")))


def sent_doctor_info_to_site(doctors_last_name):
    specialization, doctor_id = find_specialization(doctors_last_name)
    select_specialization(specialization)  # select specialisation
    select_doctor(doctor_id)


def possible_data_to_dict(appointment_dict, active_day):
    possible_days_list, time_in_active_day_list = appointment_date_and_time(appointment_dict, active_day)
    appointment_dict[active_day] = time_in_active_day_list
    return possible_days_list


def get_information_about_doctors_and_save_it():  # main function
    create_report("SMT_clinic", "appointments", 'clinic', ['doctor', 'appoinment_date', 'comments']) # create report file
    enter_cabinet()  # authorisation only

    count = 0
    for person in ['Тарасова', 'Марченко', 'Гаглоева']:
        sent_doctor_info_to_site(person)
        page_html = select_clinic()

        month, active_day, active_day_time, address, doctor_family_name, all_days = get_information_from_page(page_html)

        appointment_dict = {}
        possible_days_list = possible_data_to_dict(appointment_dict, active_day)

        for i in range(1, len(possible_days_list)):
            select_day_from_list(possible_days_list[i])
            page_html = browser.page_source
            month, active_day, active_day_time, address, doctor_family_name, all_days = get_information_from_page(
                page_html)
            possible_data_to_dict(appointment_dict, active_day)

        if address.strip() == 'Адрес приема: Московский пр-т, 22'.strip():
            print(doctor_family_name)
            print(address)
            print(month)
            for i in appointment_dict:
                print(i, appointment_dict[i])
            print("*" * 200)

        else:
            print(f'{doctor_family_name} not available in Московский пр-т, 22')
        save_data_pickle(appointment_dict,
                         doctor_family_name.replace(' ', '_'))  # сохраняю данные по интересующим меня врачам
        count += 1
        browser.get('https://clinic-complex.ru/cabinet/visits/schedule/')
        WebDriverWait(browser, 20).until(lambda d: d.find_element(By.NAME, 'EMAIL'))
    browser.close()
    browser.quit()


if __name__ == '__main__':
    browser = webdriver.Chrome(options=setting_chrome_options())
    get_information_about_doctors_and_save_it()
