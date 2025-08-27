from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser= webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    num1 = browser.find_element(By.ID,"num1").text
    num2 = browser.find_element(By.ID,"num2").text
    res=int(num1)+int(num2)
    
    answer= Select(browser.find_element(By.TAG_NAME,"select"))
    answer.select_by_value(str(res))
    
    submit = browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
    submit.click()
    
finally:
    time.sleep(50)
    browser.quit()