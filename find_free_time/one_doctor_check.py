# test with alferov

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from must_have.crome_options import setting_chrome_options



def one_doctor():
    browser = webdriver.Chrome(options=setting_chrome_options())
    browser.get('https://clinic-complex.ru/staff/vrachi/alferov_konstantin_ivanovich/')
    try:
        browser.find_element(By.CLASS_NAME, "appointment-online__form-check").click()
    except Exception as ex:
        print(ex)
    time.sleep(5)
    browser.close()
    browser.quit()


if __name__ == '__main__':
    one_doctor()