from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration1.html"
    # link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_firstname_field = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
    input_firstname_field.send_keys("sniff my first sock")
    input_lastname_field = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
    input_lastname_field.send_keys("sniff my last sock")
    input_email_field = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
    input_email_field.send_keys("sniff my websocket")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(10)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()