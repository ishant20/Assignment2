from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    username = (By.ID,"email")
    password = (By.ID,"pass")
    login = (By.NAME,"login")

    def user_name(self):
        return self.driver.find_element(*LoginPage.username)

    def user_password(self):
        return self.driver.find_element(*LoginPage.password)

    def login_button(self):
        return self.driver.find_element(*LoginPage.login)
