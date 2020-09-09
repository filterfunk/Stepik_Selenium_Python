from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

# Открываем сайт
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Заполняем поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("1")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("2")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ivan@mail.ru")

    # Прикрепляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(os.path.abspath(__file__))  # Выводим путь текущего файла Питон
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла txt
    print(file_path)  # Выводим к файлу txt
    # Ищем кнопку для прикрепления файла и отдаём в неё путь к файлу через send_keys
    input4 = browser.find_element(By.NAME, "file")
    input4.send_keys(file_path)

    # Жмём Submit
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
