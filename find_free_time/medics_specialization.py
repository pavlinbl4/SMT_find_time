from find_free_time.my_account import enter_cabinet
from find_free_time.specialization import select_specialization
from must_have.soup import get_soup
import io
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def save_html_page(browser, specialization_index):
    with io.open(browser.title + ".html", "w", encoding="utf-8") as f:
        f.write(browser.page_source)
        f.close()


def get_html(specialization_index):
    browser = enter_cabinet()
    select_specialization(specialization_index, browser)
    Select(WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "body > main > section > form > "
                                    "fieldset.appointment-online__form-fieldset.--col-2.step4 >"
                                    " label > div > select"))))
    save_html_page(browser, specialization_index)
    return browser.page_source


if __name__ == '__main__':
    soup = get_soup(get_html("32361"))
    specialists = soup.find('select', {'name': 'SPECIALIST'})
    print(specialists)