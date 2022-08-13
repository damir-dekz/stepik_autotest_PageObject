from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

LCT_ADD = (By.XPATH, "//form[@id='add_to_basket_form']/button")


def test_item(browser):
    wait = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(LCT_ADD))
    assert wait.is_displayed() == True, "Элемент не отображан на странице"
