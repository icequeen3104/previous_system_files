import pytest

@pytest.mark.smoke
@pytest.mark.skip #this is used to skip a particular test case
def test_firstProgram():
    msg = "Hello" #operation
    assert msg == "hi", "test failed because strings do not match"


@pytest.mark.xfail #this is used to run this test case but not print the output of it
def test_secondCreditCard(): #if u want to run method of specific name in the programs "test_demo.py" and "test_demo2.py" then use "py.test -k CreditCard -v -s"
    a = 4
    b = 6

    assert a+2 == 6, "Addition do not match"

@pytest.fixture()
def setup():
    print("I will execute first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")

