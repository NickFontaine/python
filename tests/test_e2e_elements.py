import pytest
from pages.elements import DuckDuckGoResultPage
from pages.home import DemoQAHomePage
from selenium.webdriver import Chrome

@pytest.fixture
def browser():
  driver = Chrome()
  driver.implicitly_wait(10)
  driver.quit()

def click_elements_section(browser):
