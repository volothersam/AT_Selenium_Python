from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from math import log, sin

with webdriver.Chrome() as driver:
    driver.maximize_window()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "$100")
    )
    driver.find_element(By.XPATH, "//button[@id='book']").click()

    x = int(driver.find_element(By.XPATH, "//*[@id='input_value']").text)
    ans = log(abs(12*sin(x)))
    driver.find_element(By.XPATH, "//*[@id='answer']").send_keys(ans)
    
    driver.find_element(By.XPATH, "//button[@id='solve']").click()

    sleep(10)