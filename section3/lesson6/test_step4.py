from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
from auth import email, password

link_list = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize("link", link_list)
def test(driver_wait, link):
    driver, wait = driver_wait
    driver.get(link)
    driver.maximize_window()

    login_button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='main-navbar']/a[contains(@href, 'login')]")
        )
    )
    login_button.click()

    login_form_xpath = "//*[@id='login_form']"
    wait.until(
        EC.visibility_of_element_located((By.XPATH, login_form_xpath))
    )
    login_email_field = driver.find_element(
        By.XPATH, f"{login_form_xpath}//*[@id='id_login_email']"
    )
    login_email_field.send_keys(email)
    login_password_field = driver.find_element(
        By.XPATH, f"{login_form_xpath}//*[@id='id_login_password']"
    )
    login_password_field.send_keys(password)
    login_button = driver.find_element(
        By.XPATH, f"{login_form_xpath}//button[@type='submit']"
    )
    login_button.click()
    wait.until(
        EC.invisibility_of_element_located((By.XPATH, login_form_xpath))
    )
    # Написать более адекватные ожидания
    answer_field = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")
        )
    )
    answer = math.log(int(time.time()))
    answer_field.send_keys(answer)
    answer_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Отправить']"))
    )
    answer_button.click()
    check_correct_hint = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[@class='smart-hints__hint']")
        )
    )
    assert check_correct_hint.text == "Correct!"