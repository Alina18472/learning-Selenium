from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")
    
    elements_required = browser.find_elements(By.CSS_SELECTOR,"input:required")
    for i in elements_required:
        i.send_keys("Мой ответ")
        
    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    
    time.sleep(1)
    
    welcome_text = browser.find_element(By.TAG_NAME,"h1")
    assert "Congratulations! You have successfully registered!" == welcome_text.text
finally:
    time.sleep(30)
    browser.quit()    