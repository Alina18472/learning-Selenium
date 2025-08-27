from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    
    book = browser.find_element(By.ID,"book")
    book.click()
    
    submit = browser.find_element(By.CSS_SELECTOR,"button[type=submit]")
    browser.execute_script("return arguments[0].scrollIntoView(true);",submit)

    x = browser.find_element(By.ID, "input_value").text
    input = browser.find_element(By.ID,"answer")
    input.send_keys(calc(x))
    
    submit.click()
    
finally:
    time.sleep(30)
    browser.quit()