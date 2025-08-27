from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    name = browser.find_element(By.CSS_SELECTOR,"[name=firstname]")
    last_name = browser.find_element(By.CSS_SELECTOR,"[name=lastname]")
    email = browser.find_element(By.CSS_SELECTOR,"[name=email]")
    name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    email.send_keys("sdfs@mail.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir,"new.txt")
    
    open = browser.find_element(By.ID,"file")
    open.send_keys(file_path)
    
    submit = browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
    submit.click()
finally:
    time.sleep(30)
    browser.quit()