from selenium import webdriver

def test_with_selenium():
    driver = webdriver.Edge()
    driver.get("http://localhost:5000/")