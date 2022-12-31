import pytest

class TestClass:
    """
    1. File names should starting with test_ or ending with _test , as in test_example.py or example_test.py
    2. Class name should start with “Test”, as in TestExample
    3. Test method names should start with “test”, as in test_example(), else the method won't be considered as test method.
    """

    def test_Method1(self):
        print("this is test method 1")

    def test_Method2(self):
        print("this is test method 2")

    def test_Method3(self):
        print("this is test method 3")


