import pytest


@pytest.fixture()
def set_up():
    print("Start test") # перед каждым тестом
    yield
    print("Finish test")


