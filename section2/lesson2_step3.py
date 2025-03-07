from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://suninjuly.github.io/selects1.html")

    num1 = int(driver.find_element(By.XPATH, "//h2/span[@id='num1']").text)
    num2 = int(driver.find_element(By.XPATH, "//h2/span[@id='num2']").text)
    ans = num1 + num2

    driver.find_element(By.XPATH, "//select[@id='dropdown']").click()
    driver.find_element(By.XPATH, f"//select[@id='dropdown']/option[@value={ans}]").click()
    driver.find_element(By.XPATH, "//button").click()

finally:
    sleep(10)
    driver.quit()