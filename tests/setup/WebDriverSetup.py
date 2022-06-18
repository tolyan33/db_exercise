import unittest

import urllib3
from selenium import webdriver


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()
