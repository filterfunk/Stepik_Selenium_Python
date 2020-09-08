from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("1")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("2")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("3")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("4")
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла