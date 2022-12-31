from loginpageobject import Login_page

class Test_Login:
    def test_valid_input(self,setup,username="admin@yourstore.com",password="admin"):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.login_page = Login_page(self.driver)  # getting the input from the Login_Page class (Page object details)
        self.login_page.set_username(username)
        self.login_page.set_password(password)
        self.login_page.click_login()
        self.status = False
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.status = True
        self.driver.close()
        assert self.status
