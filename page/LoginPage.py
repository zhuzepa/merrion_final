from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure


# https://the-internet.herokuapp.com/login

class LoginPage:
    def __init__(self,
                 driver: WebDriver):  # нужно объяснить pageobject что такое driver:WebDriver, для этого делаем импорт первой строки
        self.driver = driver  # сохраняем driver

    @allure.step('Вводим логин, пароль и нажимаем кнопку')
    def auth_as(self, username: str, password: str):
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit').click()
