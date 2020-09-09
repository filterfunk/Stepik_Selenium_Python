import time
from selenium import webdriver
import math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)


# Вводим ответ в поле
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)


# Прокручиваем вниз, чтобы футер не мешал нажимать на чек-боксы
# Отметить checkbox "I'm the robot".
option1 = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

# Выбрать radiobutton "Robots rule!"
option1 = browser.find_element(By.ID, "robotsRule")
option1.click()


button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
