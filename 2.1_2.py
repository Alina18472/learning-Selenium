from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    
    
    x_element = browser.find_element(By.CSS_SELECTOR,"#treasure")
    x = x_element.get_attribute("valuex")
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