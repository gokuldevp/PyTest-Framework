import pytest

class TestClass:
    """using the decarotor @pytest.mark.first for ordering the test methods. this is a custom method in pytest"""

    @pytest.mark.third
    def test_Method1(self):
        print("This is Method1 C")
        assert True == True

    @pytest.mark.fourth
    def test_Method2(self):
        print("This is Method2 D")
        assert True == True

    @pytest.mark.fifth
    def test_Method3(self):
        print("This is Method3 E")
        assert True == True

    @pytest.mark.first
    def test_Method4(self):
        print("This is Method4 A")
        assert True == True

    @pytest.mark.second
    def test_Method5(self):
        print("This is Method5 B")
        assert True == True
