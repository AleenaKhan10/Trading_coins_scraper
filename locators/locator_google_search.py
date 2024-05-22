from selenium.webdriver.common.by import By
from locators.locator_base_page import BasePageLocators


class GoogleSearchLocators(BasePageLocators):
    @staticmethod
    def get_homepage_xpath(url):
        if url:
            schemes = ["", "https://", "http://", "https://www.", "http://www."]
            paths = ["", "/"]
            conditions = " or ".join([f"@href = '{scheme}{url}{path}'" for scheme in schemes for path in paths])
            return (By.XPATH, f"//a[{conditions}]")
        return None
        
    @classmethod
    def get_g_img_title(cls, product_name):
        g_img_title = f'//g-img[@title="{product_name}"]'
        return (By.XPATH, g_img_title)
    
    field_search = (By.NAME, "q")
    li_articles = (By.XPATH, "//article[@ve-visible='true']")
    search_div = (By.ID, "search")
    bottstuf_div = (By.ID, "botstuff")
    btn_next_page = (By.ID, "pnnext")
    btn_more_results = (By.XPATH, "//div[./span[text()='More results']]")
    image_tab = (By.XPATH, "//div[text()='Images'] | //span[text()='Images'] | //a[text()='Images']")
    google_search_btn = (By.XPATH, "//input[@value='Google Search']")
    walmart_search_field = (By.XPATH, "//input[@title='Search walmart.com']")
    hotfrog_search_field = (By.XPATH, "//input[@placeholder='Search hotfrog.com']")
    popup_btn = (By.XPATH, "//div[text() = 'Not now']")
    cookies_popup_btn = (By.XPATH, "//div[@class='QS5gu sy4vM']")
    search_path = (By.XPATH, '//*[@id="search"]')
    botstuff_path = (By.XPATH, '//*[@id="botstuff"]')
    show_more_business = (By.XPATH, '//span[text()="More places"] | //span[text() = "More businesses"]')
    links_locator = (By.XPATH, "//div[@id='search']//a[starts-with(@href, 'http')]")

