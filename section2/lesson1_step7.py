from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/get_attribute.html")

    x = driver.find_element(By.XPATH, "//img").get_attribute("valuex")
    y = calc(x)

    answer = driver.find_element(By.XPATH, "//*[@id='answer']")
    answer.send_keys(y)

    checkbox = driver.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    checkbox.click()

    radio = driver.find_element(By.XPATH, "//*[@id='robotsRule']")
    radio.click()

    button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'btn')]")
    button.click()
finally:
   sleep(10)
   driver.quit()