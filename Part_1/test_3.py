import pytest

class TestClass:

    @pytest.fixture()     # decorator - will be executed on every test method
    def setup(self):
        """
        1. This method will be executed on every test method,
        2. The thing above the "yield" keyword is executed before the test and below the keyword is executed after.
        3. Need to be added as an parameter in the test method
        """
        # executed before every test method.
        print("\nLaunching browser...")
        print("Open application...")

        yield
        # executed after every test method
        print("Closing browser")

    def test_Signup(self, setup):
        print("this is Signup")

    def test_Login(self, setup):
        print("this is Login Test")

    def test_Search(self, setup):
        print("this is Search Test")