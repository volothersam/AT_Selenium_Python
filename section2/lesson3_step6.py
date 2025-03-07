from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from math import log, sin

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/redirect_accept.html")

    driver.find_element(By.XPATH, "//button").click()
    driver.switch_to.window(driver.window_handles[1])

    x = int(driver.find_element(By.XPATH, "//*[@id='input_value']").text)
    ans = log(abs(12*sin(x)))
    driver.find_element(By.XPATH, "//*[@id='answer']").send_keys(ans)

    driver.find_element(By.XPATH, "//button").click()
finally:
    sleep(10)
    driver.quit()