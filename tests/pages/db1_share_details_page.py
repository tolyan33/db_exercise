from re import sub

from selenium.webdriver.common.by import By

from tests.pages.Locators import DB1Locator


class DB1ShareDetails(object):
    def __init__(self, driver):
        self.driver = driver
        self.equitystory_frame = driver.find_element(By.XPATH, DB1Locator.equitystory_frame)

    def get_db1_open_price(self):
        self.driver.switch_to.frame(self.equitystory_frame)
        open_price = self.driver.find_element(By.XPATH, DB1Locator.db1_share_open_price).text
        self.driver.switch_to.default_content()
        return float(sub(r'[^\d.]', '', open_price.replace(',', '.')))
