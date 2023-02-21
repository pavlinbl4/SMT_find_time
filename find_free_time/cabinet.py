from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from must_have.crome_options import setting_chrome_options
from must_have.credentials import get_credentials
from must_have.soup import get_soup


def enter_cabinet():
    login, password = get_credentials()
    browser = webdriver.Chrome(options=setting_chrome_options())
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

    Select(WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "POPUP_SPECIALIZATION")))).select_by_value("29889")

    Select(WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "body > main > section > form > "
                                    "fieldset.appointment-online__form-fieldset.--col-2.step4 >"
                                    " label > div > select")))) \
        .select_by_value("4001454")  # 4001454 - Болдырева   4000392 - Адферов

    page_html = browser.page_source
    return page_html
    # print(browser.find_element(By.CLASS_NAME, 'active day'))

    # time.sleep(10)

    browser.close()
    browser.quit()


if __name__ == '__main__':
    soup = get_soup(enter_cabinet())
    month = soup.find('div', class_='datepicker-days').find(class_="datepicker-switch").text
    trs = soup.find('div', class_='datepicker-days').find('tbody').find_all('tr')
    active_day = soup.find('div', class_='datepicker-days').find(class_="active day").text
    other_days = soup.find('div', class_='datepicker-days').find_all(class_="new day")
    all_days = soup.find('div', class_='datepicker-days').find_all(class_="day")

    # print(f'ближайщий день  {active_day.text} {month}')
    # other_days = soup.find('div',class_='datepicker-days').find('tbody').find_all(class_="day")
    print(soup.find(class_="fio").text)
    # print(type(soup.find(class_="fio")))
    print(month)
    # print(len(trs))
    # print(type(trs))
    print(f"{active_day = }")
    print([i.text for i in all_days if  'disabled' not in i.get('class')])
    print([i.text for i in other_days])
    # for tr in trs:
    #     for i in tr.find_all('td'):
    #         print(i)
    #         print(i.find("td", class_="new day disabled"))
    #         print(type(i))
    #     # print(tr.find_all('td', class_="active day"))
