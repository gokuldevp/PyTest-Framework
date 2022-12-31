import pytest

class TestClass:

    """
    1. parameterization - we can execute the test with different sets of data.
    2. we user the decarator as @pytest.mark.parametrize() for parameterization
    3. we add the parameter in the decarator as shown below
    """
    @pytest.mark.parametrize('num1,num2', [(2,1), (2,2), (2,3), (2,4)])
    def test_calculation(self, num1, num2):
        assert num2 % num1 == 0