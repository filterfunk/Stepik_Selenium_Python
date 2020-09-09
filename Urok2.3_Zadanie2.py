from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Нажимаем на первую кнопку
button = browser.find_element(By.TAG_NAME, "button")
button.click()

# Переходим на новую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# Решаем капчу для роботов и отправляем
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)


input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element_by_tag_name("button")
button.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
