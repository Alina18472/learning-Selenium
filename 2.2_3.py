from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    res = calc(x)
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(res)
    
    checkbox= browser.find_element(By.ID,"robotCheckbox")
    checkbox.click()
    
    rad_btn= browser.find_element(By.ID,"robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);",rad_btn)
    rad_btn.click()
    
    submit= browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
    submit.click()
finally:
    time.sleep(30)
    browser.quit()