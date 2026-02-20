#lec 78
import pytest

@pytest.mark.usefixture("setup")

class TestExample:
    def test_fixtureDemo(setup):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(setup):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(setup):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(setup):
        print("I will execute steps in fixtureDemo3 method")