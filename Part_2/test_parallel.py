import pytest

class TestLogin:

    def test_login_Chrome(self):
        a = 0
        for i in range(10000):
            a += i
            for i in range(10000):
                a += i
        assert a > 1

    def test_login_Firefox(self):
        a = 0
        for i in range(10000):
            a += i
            for i in range(10000):
                a += i
        assert a < 1

    def test_login_edge(self):
        a = 0
        for i in range(10000):
            a += i
            for i in range(10000):
                a += i
        assert a == 1
