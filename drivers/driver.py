from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:

    def __init__(self):
        self.driver = None
        self.browser_name = None

    def open_browser(self):
        self.driver = webdriver.Chrome()

        driver = self.driver

        return driver
