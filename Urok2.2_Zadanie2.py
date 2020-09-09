from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Открываем сайт
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ищем значения х и у на странице и их сумму
x = browser.find_element(By.ID, "num1").text
y = browser.find_element(By.ID, "num2").text
sum = str(int(x) + int(y))
print(sum)

# Выбираем из списка ответ
select = Select(browser.find_element_by_css_selector("#dropdown"))
select.select_by_value(sum)
browser.find_element_by_css_selector(".btn").click()

time.sleep(10)
browser.quit()
