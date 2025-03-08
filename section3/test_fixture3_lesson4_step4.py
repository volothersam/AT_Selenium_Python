import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def driver():
    print("\nstart driver for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit driver..")
    driver.quit()

class TestMainPage1():
    def test_guest_should_see_ogin_link(self, driver):
        driver.get(link)
        driver.find_element(
            By.XPATH,
            "//*[contains(@class,'basket-mini')]//*[@class='btn-group']/a"
        )