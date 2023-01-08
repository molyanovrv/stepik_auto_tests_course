from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try: 
  browser = webdriver.Chrome()
  # говорим WebDriver ждать все элементы в течение 5 секунд
  browser.implicitly_wait(5)
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )
  button = browser.find_element(By.CSS_SELECTOR, "#book")
  button.click()
  x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
  y = str(math.log(abs(12*math.sin(int(x)))))
  browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
  button = browser.find_element(By.CSS_SELECTOR, "#solve")
  button.click()

  time.sleep(9)


finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  time.sleep(1)
  # закрываем браузер после всех манипуляций
  browser.quit()
