from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/file_input.html")

    inputs = driver.find_elements(By.XPATH, "//div[@class='form-group']/input")
    for input in inputs:
        input.send_keys("sniff my socks")

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)

    driver.find_element(By.XPATH, "//*[@id='file']").send_keys(file_path)

    driver.find_element(By.XPATH, "//button").click()
finally:
    sleep(10)
    driver.quit()