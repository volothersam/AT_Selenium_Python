import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome()
    return driver

class TestMainPage1():
    def test_guest_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element(By.XPATH, "//*[@id='login_link']")
    def test_guest_should_see_basket_link_on_the_main_page(seld, driver):
        driver.get(link)
        driver.find_element(
            By.XPATH,
            "//*[contains(@class,'basket-mini')]//*[@class='btn-group']/a"
        )