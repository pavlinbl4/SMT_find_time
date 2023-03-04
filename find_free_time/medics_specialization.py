from find_free_time.my_account import enter_cabinet
from find_free_time.specialization import select_specialization
from must_have.make_subfolder import m_subfolder
from must_have.soup import get_soup
import io
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def save_html_page(browser):
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
    save_html_page(browser)
    return browser.page_source


def save_doctors_to_txt(specialization_index):

    soup = get_soup(get_html(specialization_index))
    specialists = soup.find('select', {'name': 'SPECIALIST'})
    medics = specialists.find_all('option')
    with open(f'{m_subfolder("Medics")}/{specialization_index}', 'w') as input_file:
        for x in medics:
            input_file.write(f'{x.get("value")} - {x.text}\n')


if __name__ == '__main__':
    save_doctors_to_txt("6108")  #if code incorrect ??
    # specialization_index = "6108"
    # soup = get_soup(get_html(specialization_index))
    # specialists = soup.find('select', {'name': 'SPECIALIST'})
    # medics = specialists.find_all('option')
    # with open(f'{m_subfolder("Medics")}/{specialization_index}', 'w') as input_file:
    #     for x in medics:
    #         input_file.write(f'{x.get("value")} - {x.text}\n')
