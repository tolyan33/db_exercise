import os
import unittest

import yfinance

from tests.pages.db1_home_page import DB1Home
from tests.setup.WebDriverSetup import WebDriverSetup


class TestDB1OpenPrice(WebDriverSetup):
    def setUp(self):
        super().setUp()
        self.home_page = DB1Home(self.driver, 'DE')

    def test_Share_Open_Price(self):

        # Accept Cookies
        self.home_page.accept_cookies()

        # Navigate to 'Share and bonds' page
        db_share_and_bonds_page = self.home_page.navigate_to_share_price_details_page()

        # Get DB1 open price
        db_open_price = db_share_and_bonds_page.get_db1_open_price()

        # Get DB1 open price from 3rd party service provider
        db_open_price_ext = yfinance.Ticker("DB1.DE").info['open']

        # Compare open price from web portal and 3rd party service provider
        self.assertEqual(db_open_price_ext, db_open_price, "TestDB1OpenPrice failed")

        # Print info to the console
        print("DB1 Open Price: {:.2f}".format(db_open_price), "TestDB1OpenPrice completed successfully", sep=os.linesep)


if __name__ == '__main__':
    unittest.main()

# install dependencies
# readme
# investigate inheritance of general class