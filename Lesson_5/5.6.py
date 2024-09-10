from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/login")
    input_name = chrome.find_element(By.ID, "username")
    input_name.send_keys("tomsmith")
    sleep(1)
    input_pass = chrome.find_element(By.ID, "password")
    input_pass.send_keys("SuperSecretPassword!")
    sleep(2)

    firefox.get("http://the-internet.herokuapp.com/login")
    input_name = firefox.find_element(By.ID, "username")
    input_name.send_keys("tomsmith")
    sleep(1)
    input_pass = firefox.find_element(By.ID, "password")
    input_pass.send_keys("SuperSecretPassword!")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()