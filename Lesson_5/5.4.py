import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(chrome, 10)
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clicable(
        (By.CSS_SELECTOR, "modal-footer")))
    time.sleep(3)
    close_button.click()
        time.sleep(2)
    
    firefox.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(firefox, 10)
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clicable(
        (By.CSS_SELECTOR, "modal-footer")))
    time.sleep(3)
    close_button.click()
        time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.quit()