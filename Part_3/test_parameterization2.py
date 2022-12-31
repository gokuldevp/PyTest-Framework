import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestClass:
    @pytest.mark.parametrize("username,password",
                             [("Admin","admin123"),
                              ("Admin","password"),
                              ("username","admin123"),
                              ("admin123","Admin")])
    def test_login(self, username, password):
        self.serv_obj = Service("D:\Development\driver\Chrome\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "oxd-button").click()

        self.status = self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").is_displayed()
        self.driver.close()
        assert self.status

