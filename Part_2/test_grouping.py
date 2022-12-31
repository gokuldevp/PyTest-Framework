import pytest

class TestClass:
    """use the decarator @pytest.mark.sanity for skipping the the method, where sanity is custom marker."""

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SignupByEmail(self):
        print("This is Signup by Email...")
        print("part of sanity and regression")
        assert True == True

    @pytest.mark.sanity
    def test_SignupByFacebook(self):
        print("This is Signup by Facebook...")
        print("part of sanity")
        assert True == True

    @pytest.mark.sanity
    def test_SignupByTwitter(self):
        print("This is Signup by Twitter...")
        print("part of sanity")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByEmail(self):
        print("This is login by Email...")
        print("part of sanity and regression")
        assert True == True


    @pytest.mark.regression
    def test_LoginByFacebook(self):
        print("This is login by Facebook...")
        print("part of regression")
        assert True == True


    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is login by Twitter...")
        print("part of regression")
        assert True == True