from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def scenario(link):
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, "div.first_block input.first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.second").send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, "div.first_block input.third").send_keys("Ivan@ov.ru")
    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    h1 = welcome_text_elt.text
    return h1


class TestText(unittest.TestCase):
 def test_regForm1(self):
    link = "http://suninjuly.github.io/registration1.html"
    h1 = scenario(link)
    print(h1)
    print("Congratulations! You have successfully registered!" == h1)
    print("===")
    self.assertEqual("Congratulations! You have successfully registered!", h1, f'Has no congrat on {link}')

 def test_regForm2(self):
    link = "http://suninjuly.github.io/registration2.html"
    h1 = scenario(link)
    print(h1)
    print("Congratulations! You have successfully registered!" == h1)
    print("===")
    self.assertEqual("Congratulations! You have successfully registered!", h1, f'Has no congrat on {link}')


if __name__ == "__main__":
  unittest.main()
  # закрываем браузер после всех манипуляций
  browser.quit()