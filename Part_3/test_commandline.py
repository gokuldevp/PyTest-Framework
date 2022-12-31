import pytest
from selenium.webdriver.common.by import By


class TestCLI:
    @pytest.mark.test_id("TC-001")
    @pytest.mark.test_description("Test scenario: Login Test")
    @pytest.mark.parametrize("username,password",
                             [("Admin","admin123"),
                              ("Admin","password"),
                              ("username","admin123"),
                              ("admin123","Admin")])
    def test_login(self,setup, username, password):
        # python log in test
        self.driver = setup
        self.driver.implicitly_wait(2)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "oxd-button").click()
        # self.status = self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").is_displayed()
        self.status = False
        if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
            self.status = True
            print("Test ")
        self.driver.close()
        assert self.status