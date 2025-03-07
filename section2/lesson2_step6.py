from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://suninjuly.github.io/execute_script.html")

    x = int(driver.find_element(By.XPATH, "//*[@id='input_value']").text)
    ans = log(abs(12*sin(x)))
    driver.find_element(By.XPATH, "//*[@id='answer']").send_keys(ans)

    button = driver.find_element(By.XPATH, "//button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)

    driver.find_element(By.XPATH, "//*[@id='robotCheckbox']").click()
    driver.find_element(By.XPATH, "//*[@id='robotsRule']").click()

    button.click()
finally:
    sleep(10)
    driver.quit()