from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():
    @classmethod
    def setup_class(cls):
        print("\nstart driver for test suite..")
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("quit driver for test suite..")
        cls.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element(By.XPATH, "//*[@id='login_link']")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.driver.get(link)
        self.driver.find_element(
            By.XPATH, "//*[contains(@class,'basket-mini')]//*[@class='btn-group']/a"
        )
    
class TestMainPage2():
    def setup_method(self):
        print("start driver for test..")
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print("quit driver for test..")
        self.driver.quit()

    def test_guest_should_see_login_link(self):
        self.driver.get(link)
        self.driver.find_element(By.XPATH, "//*[@id='login_link']")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.driver.get(link)
        self.driver.find_element(
            By.XPATH, "//*[contains(@class,'basket-mini')]//*[@class='btn-group']/a"
        )