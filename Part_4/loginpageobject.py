from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_page:
    # Locators
    txtbox_username_id = "Email"
    txtbox_password_id = "Password"
    button_login_class = "login-button"

    # constructor
    def __init__(self, driver):
        self.driver=driver

    # Action Methods
    def set_username(self, username):
        usernametxt = self.driver.find_element(By.ID, self.txtbox_username_id)
        usernametxt.clear()
        usernametxt.send_keys(username)

    def set_password(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.txtbox_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, self.button_login_class).click()



