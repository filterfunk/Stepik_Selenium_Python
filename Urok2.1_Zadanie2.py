from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

# Открываем сайт
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


# Считаем по формуле ответ
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Ищем значение Х
x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

# Вводим ответ в поле
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

# Отметить checkbox "I'm the robot".
option1 = browser.find_element(By.ID, "robotCheckbox")
option1.click()

# Выбрать radiobutton "Robots rule!"
option1 = browser.find_element(By.ID, "robotsRule")
option1.click()

button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
# не забываем оставить пустую строку в конце файла
