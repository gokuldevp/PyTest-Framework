import pytest

class TestClass:
    """using the decarotor @pytest.mark.run(order=1) for ordering the test methods. this is a default method in pytest"""
    @pytest.mark.run(order=3)
    def test_Method1(self):
        print("This is Method1 C")
        assert True == True

    @pytest.mark.run(order=4)
    def test_Method2(self):
        print("This is Method2 D")
        assert True == True

    @pytest.mark.run(order=5)
    def test_Method3(self):
        print("This is Method3 E")
        assert True == True

    @pytest.mark.run(order=1)
    def test_Method4(self):
        print("This is Method4 A")
        assert True == True

    @pytest.mark.run(order=2)
    def test_Method5(self):
        print("This is Method5 B")
        assert True == True
