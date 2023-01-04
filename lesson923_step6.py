from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    #select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    #select.select_by_value(str(y))
    
#    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']").send_keys("first name")
#    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']").send_keys("last name")
#    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']").send_keys("email")

#    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
#    file_path = os.path.join(current_dir, 'lesson922_step8.py.txt')           # добавляем к этому пути имя файла 
#    element = browser.find_element(By.CSS_SELECTOR, "#file")
#    element.send_keys(file_path)

#    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()

#    input1 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
#    input1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
#    browser.switch_to.alert.accept()
    newtab = browser.window_handles[1]
    browser.switch_to.window(newtab)
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    #x2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    y = calc(x)
    #time.sleep(3)
    print(x, "  ",y)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()


    time.sleep(9)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    #browser.quit()

#print(os.path.abspath(__file__))
#print(os.path.abspath(os.path.dirname(__file__)))