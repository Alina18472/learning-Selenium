from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    
    
    x = browser.find_element(By.CSS_SELECTOR,"#input_value").text
    input = browser.find_element(By.ID, "answer")
    input.send_keys(calc(x))
    
    checkbox = browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()
    
    rad_btn = browser.find_element(By.ID,"robotsRule")
    rad_btn.click()
    
    submit = browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
    submit.click()
    
finally:
    time.sleep(50)
    browser.quit()