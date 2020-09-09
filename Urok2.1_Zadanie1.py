from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

# Открываем сайт
link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

# Ищем значение Х
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text


# Считаем по формуле ответ
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)

# Вводим ответ в поле
input1 = browser.find_element(By.CLASS_NAME, "form-control")
input1.send_keys(y)

# Отметить checkbox "I'm the robot".
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

# Выбрать radiobutton "Robots rule!"
option1 = browser.find_element_by_css_selector("[for='robotsRule']")
option1.click()

button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
button.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
# не забываем оставить пустую строку в конце файла
