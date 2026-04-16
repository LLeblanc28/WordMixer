from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import pytest


@pytest.fixture()
def driver():
    load_dotenv()
    run_selenium_local = bool(os.getenv('RUN_SELENIUM_LOCAL', False))
    if run_selenium_local:
        service = webdriver.ChromeService(executable_path=os.getenv('CHROMEDRIVER_PATH'))
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.binary_location = os.getenv('CHROMEBIN_PATH')
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = webdriver.Remote(command_executor='http://localhost:4444', options=webdriver.FirefoxOptions())
        driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture()
def target_host():
    load_dotenv()
    return os.getenv('TARGET_HOST', 'localhost')

@pytest.fixture()
def target_port():
    load_dotenv()
    return os.getenv('TARGET_PORT', '5000')

@pytest.fixture()
def target_scheme():
    load_dotenv()
    return os.getenv('TARGET_SCHEME', 'http')

def test_with_selenium(driver, target_scheme, target_host, target_port):
    driver.get(f"{target_scheme}://{target_host}:{target_port}")
    # input text
    input_word = driver.find_element(by=By.ID, value="word")
    input_word.send_keys("hello")
    # click on submit
    submit_button = driver.find_element(
        by=By.XPATH, value="/html/body/form/div[2]/input"
    )
    submit_button.click()
    # check the result on the redirected page
    result_shuffled_word = driver.find_element(by=By.XPATH, value="/html/body")
    assert "hello" != result_shuffled_word.text
    
def test_do_not_found(driver, target_scheme, target_host, target_port):
    driver.get(f"{target_scheme}://{target_host}:{target_port}")
    with pytest.raises(NoSuchElementException):
        driver.find_element(by=By.ID, value='none')

def test_do_not_found_empty(driver, target_scheme, target_host, target_port):
    driver.get(f"{target_scheme}://{target_host}:{target_port}")
    result = driver.find_elements(by=By.ID, value='none')
    assert len(result) == 0