from selenium import webdriver
from page.LoginPage import LoginPage


def test_ya(login_page: LoginPage, test_data_login: dict):
    login_page.auth_as(test_data_login.get('user'), test_data_login.get('password'))
