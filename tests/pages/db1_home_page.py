from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from tests.pages.Locators import DB1Locator
from tests.pages.db1_share_details_page import DB1ShareDetails


class DB1Home(object):
    def __init__(self, driver,  version='EN'):
        self.driver = driver

        # For german version use: dbg-de
        url = 'https://deutsche-boerse.com/' + ('dbg-en' if version=='EN' else 'dbg-de')

        self.driver.get(url)

        self.db1_investor_relations = driver.find_element(By.XPATH, DB1Locator.db1_investor_relations)
        self.db1_share_and_bonds = driver.find_element(By.XPATH, DB1Locator.db1_share_and_bonds)
        self.db1_accept_cookies = driver.find_element(By.ID, DB1Locator.db1_accept_cookies)

    def navigate_to_share_price_details_page(self):
        # TODO: for small resolutions Main Navigation appears
        action = ActionChains(self.driver)
        action.move_to_element(self.db1_investor_relations).perform()
        self.db1_share_and_bonds.click()
        return DB1ShareDetails(self.driver)

    def accept_cookies(self):
        self.db1_accept_cookies.click()
