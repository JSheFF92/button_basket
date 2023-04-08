import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_190/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket_button, 'Basket button not found'
    time.sleep(30)

