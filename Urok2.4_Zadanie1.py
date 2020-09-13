from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from math import log, sin

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 15 секунд, цена не станет 100
WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))

browser.find_element_by_id('book').click()

browser.find_element_by_id('answer').send_keys(
  str(log(abs(12*sin(int(browser.find_element_by_id('input_value').text)))))
)
browser.find_element_by_id('solve').click()

time.sleep(5)
browser.quit()
