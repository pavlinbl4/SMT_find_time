from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from must_have.crome_options import setting_chrome_options
from must_have.credentials import get_credentials


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

    return browser


if __name__ == '__main__':
    enter_cabinet()
