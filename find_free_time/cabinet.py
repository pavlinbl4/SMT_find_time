from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from must_have.crome_options import setting_chrome_options
from must_have.credentials import get_credentials


import time


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

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "--online-order")))
    browser.find_element(By.CLASS_NAME, "--online-order").click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "appointment-online__form")))


    Select(WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "POPUP_SPECIALIZATION")))).select_by_value("29889")

    Select(WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "body > main > section > form > fieldset.appointment-online__form-fieldset.--col-2.step4 > label > div > select")))).select_by_value("4000392")


    print(browser.find_element(By.CLASS_NAME, 'active day'))







    time.sleep(10)

    browser.close()
    browser.quit()







if __name__ == '__main__':
    enter_cabinet()
