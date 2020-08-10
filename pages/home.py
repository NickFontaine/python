from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class DemoQAHomePage:
  URL = 'https://www.demoqa.com'

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(self.URL)
