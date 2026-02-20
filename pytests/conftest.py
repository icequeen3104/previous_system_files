import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("i will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Rahul", "shetty"), ("Firefox","Rahul"), ("IE", "SS")])
def crossBrowser(request):
    return request.param
