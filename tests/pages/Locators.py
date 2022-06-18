class DB1Locator(object):

    # Locators for Deutsche-Boerse Home Page - https://www.deutsche-boerse.com
    db1_investor_relations = "//a[.='Investor relations' or .='Investor Relations']"
    db1_share_and_bonds = "//a[.='Share and bonds' or .='Aktie und Anleihen']"
    db1_accept_cookies = "cookiescript_accept"

    # Locators for Share Details Page - https://www.deutsche-boerse.com/dbg-de/investor-relations/aktie-und-anleihen
    equitystory_frame = "//*[@class='easyxdm-iframe']/iframe"
    db1_share_open_price = "//*[@id='top-table']//td[contains(.,'Open')]/following-sibling::td[@class='col2']"

