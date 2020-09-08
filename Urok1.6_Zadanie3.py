#Заполнить все поля через find_elements
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:

    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input[type=text]")
    for element in elements:
        element.send_keys("Hello")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
