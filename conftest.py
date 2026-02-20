import pytest
from selenium import webdriver


# Add the --browser_name argument to the command line
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


# Define the browserInstance fixture to create the appropriate browser instance
@pytest.fixture(scope="function")
def browserInstance(request):  # You need to access the request object here
    browser_name = request.config.getoption("--browser_name")  # Get the browser name from pytest options

    # Initialize WebDriver based on selected browser
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)  # Optional: Only if you want a default implicit wait

    yield driver  # Yield the driver to the test function execution

    driver.quit()  # Quit the driver after the test
