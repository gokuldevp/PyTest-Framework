import pytest

class TestClass:

    @pytest.fixture()     # decorator - will be executed on every test method
    def setup(self):
        # executed before every test method.
        print("\nLaunching browser...")
        print("Open application...")

    def test_Signup(self, setup):
        print("this is Signup")

    def test_Login(self, setup):
        print("this is Login Test")

    def test_Search(self, setup):
        print("this is Search Test")