from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from must_have.crome_options import setting_chrome_options
from must_have.credentials import get_credentials
from must_have.soup import get_soup


def select_specealization(specialization_index):
    Select(WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "POPUP_SPECIALIZATION")))).select_by_value(specialization_index)


def select_doctor(doctor_index):
    Select(WebDriverWait(browser, 40).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "body > main > section > form > "
                                    "fieldset.appointment-online__form-fieldset.--col-2.step4 >"
                                    " label > div > select")))) \
        .select_by_value(doctor_index)


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

    select_specealization("29889")

    select_doctor("4001454")  # 4001454 - Болдырева   4000392 - Адферов

    browser.find_element(By.XPATH, '/html/body/main/section/form/fieldset[9]/label[2]/span').click()

    page_html = browser.page_source
    return page_html

    browser.close()
    browser.quit()


if __name__ == '__main__':
    browser = webdriver.Chrome(options=setting_chrome_options())
    soup = get_soup(enter_cabinet())
    month = soup.find('div', class_='datepicker-days').find(class_="datepicker-switch").text
    trs = soup.find('div', class_='datepicker-days').find('tbody').find_all('tr')
    active_day = soup.find('div', class_='datepicker-days').find(class_="active day").text
    other_days = soup.find('div', class_='datepicker-days').find_all(class_="new day")
    all_days = soup.find('div', class_='datepicker-days').find_all(class_="day")

    doctor_family_name = soup.find(class_="fio").text

    address = soup.find(class_='data__item data__item__address').text

    active_day_time = soup.find(class_="spanSelectors").find_all('span', class_="time")

    print(doctor_family_name)
    print(address)
    print(month)

    time_in_active_day_list = [x.text for x in active_day_time]

    aviable_days_list = [i.text for i in all_days if 'disabled' not in i.get('class')]
    print(f'{aviable_days_list = }')

    print(f"{active_day = }")
    print(f"{time_in_active_day_list = }")
