import pytest
"""
1. The file name should be conftest.py while creating the configuration file.
2. The conftest.py need to be created in the same directory as the other file.
"""

@pytest.fixture()  # decorator - will be executed on every test method
def setup():
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
    print("\nClosing browser")