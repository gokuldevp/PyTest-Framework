import pytest

class TestClass:
    """
    using the decarotor @pytest.mark.dependency() for dependency test method,
    if depended test method is not passed, then the depended test method is skipped.
    """

    @pytest.mark.dependency()
    def test_openapp(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_openapp'])
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_search(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_login', 'TestClass::test_search'])
    def test_advsearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_logout(self):
        assert True