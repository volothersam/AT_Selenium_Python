import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver_wait():
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)
    yield driver, wait
    driver.quit()