import time
from selenium import webdriver


browser = webdriver.Chrome()
browser.get()

#alert('Hello!');
alert = browser.switch_to.alert
alert.accept()

time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()
