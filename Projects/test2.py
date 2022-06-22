from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




ser = Service("/usr/local/bin/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

def test_login_prism():
    driver.get("https://pa-develop.bdtrust.org/login")

    assert driver.find_element(By.NAME, "user[user_name]")
    assert driver.find_element(By.NAME, "user[password]")
    assert driver.find_element(By.ID, "submit")