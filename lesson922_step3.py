from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    x2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    y = x + x2
#    time.sleep(3)
    print(x, "  ", x2, "  ",y)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    #select.select_by_visible_text(y)
    select.select_by_value(str(y))
    
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(9)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    #browser.quit()