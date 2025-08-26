from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")
    
    first_name = browser.find_element(By.CSS_SELECTOR,"input[placeholder = 'Input your first name']")
    last_name = browser.find_element(By.CSS_SELECTOR,"input[placeholder = 'Input your last name']")
    email = browser.find_element(By.CSS_SELECTOR,"input[placeholder = 'Input your email']") 
    
    first_name.send_keys('Ivan')
    last_name.send_keys("Petrov")
    email.send_keys("sfdsa@mail.ru")
    
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    
    time.sleep(1)
    
    welcome_text = browser.find_element(By.TAG_NAME,"h1")
    assert "Congratulations! You have successfully registered!" == welcome_text.text
finally:
    time.sleep(30)
    browser.quit()    