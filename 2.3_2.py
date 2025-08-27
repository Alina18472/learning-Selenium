from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    
    button = browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
    button.click()
    
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    
    browser.switch_to.window(second_window)
    
    x = browser.find_element(By.ID,"input_value").text 
    input = browser.find_element(By.ID,"answer")
    input.send_keys(calc(x))
    
    submit = browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
    submit.click()
finally:
    time.sleep(50)
    browser.quit()