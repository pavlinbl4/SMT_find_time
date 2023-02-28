from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from must_have.crome_options import setting_chrome_options




def select_specialization(specialization_index, browser):
    Select(WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "POPUP_SPECIALIZATION")))).select_by_value(specialization_index)