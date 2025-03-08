import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class Testing(unittest.TestCase):
    def test_lesson6_step10_registration1(self):
        with webdriver.Chrome() as driver:
            link = "http://suninjuly.github.io/registration1.html"
            driver.get(link)
            field_firstname = driver.find_element(
                By.XPATH, "//div[@class='first_block']//input[contains(@class, 'first')]"
            )
            field_firstname.send_keys('sniff my first sock')
            field_lastname = driver.find_element(
                By.XPATH, "//div[@class='first_block']//input[contains(@class, 'second')]"
            )
            field_lastname.send_keys('sniff my second sock')
            field_email = driver.find_element(
                By.XPATH, "//div[@class='first_block']//input[contains(@class, 'third')]"
            )
            field_email.send_keys('sniff my websocket')
            driver.find_element(By.XPATH, "//button").click()
            welcome_text_check = WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, "//h1"),
                    "Congratulations! You have successfully registered!"
                )
            )
            # driver.implicitly_wait(5)
            # welcome_text = driver.find_element(By.XPATH, "//h1").text
            # print(welcome_text)
            self.assertTrue(welcome_text_check)

    def test_lesson6_step10_registration2(self):
        with webdriver.Chrome() as driver:
            link = "http://suninjuly.github.io/registration2.html"
            driver.get(link)
            field_firstname = driver.find_element(
                By.XPATH, "//div[@class='first_block']//input[contains(@class, 'first')]"
            )
            field_firstname.send_keys('sniff my first sock')
            field_lastname = driver.find_element(
                By.XPATH, "//div[@class='first_block']//input[contains(@class, 'second')]"
            )
            field_lastname.send_keys('sniff my second sock')
            field_email = driver.find_element(
                By.XPATH, "//div[@class='first_block']//input[contains(@class, 'third')]"
            )
            field_email.send_keys('sniff my websocket')
            driver.find_element(By.XPATH, "//button").click()
            welcome_text_check = WebDriverWait(driver, 5).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, "//h1"),
                    "Congratulations! You have successfully registered!"
                )
            )
            # welcome_text = driver.find_element(By.XPATH, "//h1").text
            # print(welcome_text)
            self.assertTrue(welcome_text_check)

if __name__ == "__main__":
    unittest.main()