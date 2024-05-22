from selenium.webdriver.common.by import By

class CoinsLocator:

    gems_locator = (By.XPATH, '//div[text() = "Find Gems"]/following-sibling::a')
    headers_locator = (By.XPATH, '//thead[@class="ant-table-thead"]/tr/th')
    rows_locator = (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr')
    next_pg_btn_locator = (By.XPATH, '//span[@aria-label="right"]')
    solana_tab = (By.XPATH, '//button[@type="button"]/span[text() = "Solana"]')
    captcha = (By.XPATH, '//input[@type = "checkbox"]')
    iframe = (By.XPATH, '//iframe')