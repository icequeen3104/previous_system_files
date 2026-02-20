#lec 73 74 75
#any pytest file should start with test_ or end with _test
#pytest method names should start with test
#any code should be wrapped in method only
# "-v" keyword in terminal stands for "virgos" that gives more information about the test cases
# "-s" keyword prints the output of the test cases
# -k stands for method names execution
#u can run specific file with py.test <filename>
#u can mark (tag) tests @pytest.mark.smoke and then run with -m
#methods should make sense according to whatever u want to run
#fixtures are used for setup and tear down methods for test cases- conftest file to generalize
#fixture and make it available to all test cases
#datadriven and parameterisation can be done with return statements in tuple format
#when u define fixture scope to class only, it will run once before class is initiated and at the end
#when u want to run all the test cases with html then write "pytest -s --html=report.html" in terminal
#this is basically html report generation for pytests execution

import pytest

@pytest.mark.smoke
def test_firstProgram():
    print("hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
