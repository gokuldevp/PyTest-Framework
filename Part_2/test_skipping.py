import pytest

class TestClass:
    """use the decarator @pytest.mark.skip for skipping the the method"""

    def test_SignupByEmail(self):
        print("This is Signup by Email...")
        assert True == True

    def test_SignupByFacebook(self):
        print("This is Signup by Facebook...")
        assert True == True

    def test_SignupByTwitter(self):
        print("This is Signup by Twitter...")
        assert True == True

    @pytest.mark.skip
    def test_LoginByEmail(self):
        print("This is login by Email...")
        assert True == True

    @pytest.mark.skip
    def test_LoginByFacebook(self):
        print("This is login by Facebook...")
        assert True == True

    @pytest.mark.skip
    def test_LoginByTwitter(self):
        print("This is login by Twitter...")
        assert True == True