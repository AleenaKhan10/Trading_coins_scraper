from pages.base_page import BasePage
from locators.locator_google_search import GoogleSearchLocators
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from common_components import utilities, constants



class GoogleSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_next_page_button(self):
        btn_next_page = self.wait_for_element(GoogleSearchLocators.btn_next_page, self.random_wait_time(), silent=True)
        if btn_next_page:
            return btn_next_page
        return self.wait_for_element(GoogleSearchLocators.btn_more_results, self.random_wait_time(), silent=True)
    
    def enter_text(self, by_locator,  text: str, google_url = constants.URL_GOOGLE_SEARCH) -> None:
        """ 
        Performs text entry of the passed in text, in a web element whose locator is passed to it
        """
        for _ in range(constants.MIN_COUNT):
            try:
                if google_url == self.driver.current_url or google_url == self.driver.current_url[:-1]:
                    utilities.log_message("trying to search for keyword: Method No. 1")
                    self.driver.execute_script("window.onfocus")
                    element = self.wait_for_element(by_locator, self.random_wait_time(), silent=True)
                    
                    try:
                        self.move_mouse_to_element(element)
                        for one in text:
                            element.send_keys(one)
                            utilities.random_sleep(0.05, 0.30)
                        element.submit()
                    except Exception as e:
                        utilities.log_message(e)
                    if google_url == self.driver.current_url or google_url == self.driver.current_url[:-1]:
                        utilities.log_message("trying to search for keyword: Method No. 2")
                        self.move_click_to_element(text)
                        self.press_enter_on_element(by_locator)
                        search_btn = self.wait_for_element(GoogleSearchLocators.google_search_btn, self.random_wait_time(), silent=True)
                        if search_btn:
                            self.click(search_btn)
                        if google_url == self.driver.current_url or google_url == self.driver.current_url[:-1]:
                            utilities.log_message("trying to search for keyword: Method No. 3")
                            actions = ActionChains(self.driver)
                            self.press_enter_on_element(by_locator)
                            for one in text:
                                actions.send_keys(one).perform()
                                utilities.random_sleep(0.05, 0.30)
                            self.press_enter_on_element(by_locator)
                            search_btn = self.wait_for_element(GoogleSearchLocators.google_search_btn, self.random_wait_time(), silent=True)
                            if search_btn:
                                self.click(search_btn)
                            if google_url == self.driver.current_url or google_url == self.driver.current_url[:-1]:
                                utilities.log_message("trying to search for keyword: Method No. 4")
                                self.move_click_to_google_search(text)
                                self.press_enter_on_element(by_locator)
                            else:
                                return
                        else:
                            return
                    else:
                        return
                else:
                    return
            except TimeoutException:
                self.driver.get(google_url)
            except StaleElementReferenceException:
                self.driver.get(google_url) 
                
    def enter_text_walmart(self, keyword):
        super().enter_text(GoogleSearchLocators.walmart_search_field, keyword)
        self.press_enter_on_element(GoogleSearchLocators.walmart_search_field)
                
    def search_keyword_walmart(self, keyword):
        try:
            self.enter_text_walmart(keyword)
        except StaleElementReferenceException:
            self.enter_text_walmart(keyword)
            
    def enter_text_hotfrog(self, keyword):
        super().enter_text(GoogleSearchLocators.hotfrog_search_field, keyword)
        self.press_enter_on_element(GoogleSearchLocators.hotfrog_search_field)
                
    def search_keyword_hotfrog(self, keyword):
        try:
            self.enter_text_hotfrog(keyword)
        except StaleElementReferenceException:
            self.enter_text_hotfrog(keyword)
        
    def search_keyword_after_google_search(self, keyword):
        google_field = self.wait_for_element(GoogleSearchLocators.field_search)
        self.move_mouse_to_element(google_field)
        super().enter_text(GoogleSearchLocators.field_search, keyword)
        self.press_enter_on_element(GoogleSearchLocators.field_search)
                    
    def search_keyword(self,keyword, google_url):
        self.enter_text(GoogleSearchLocators.field_search, keyword, google_url)

    def press_enter(self):
        self.press_enter_on_element(GoogleSearchLocators.field_search)
    
    def search_beta_product(self,product_name):
        g_img_title_locator = GoogleSearchLocators.get_g_img_title(product_name)
        search_div = self.wait_for_element(GoogleSearchLocators.search_div)
        matched_links_elements = self.search_element_wait_for_elements(search_div,g_img_title_locator, silent=True)
        return self.matched_wildcard_click(matched_links_elements)
    
    def search_click_wildcard(self,wildcard_string):
        self.click_location_popup()
        wildcard_locator = GoogleSearchLocators.get_wildcard_searchable(wildcard_string)
        search_div = self.wait_for_element(GoogleSearchLocators.search_div, self.random_wait_time(), silent=True)
        bottstuf_div = self.wait_for_element(GoogleSearchLocators.bottstuf_div, self.random_wait_time(), silent=True)
        print("Search Div : ", search_div)
        print("bottstuf Div : ", bottstuf_div)
        if search_div is None and bottstuf_div is None:
            self.save_page_html()
            return False

        matched_links_elements = self.wait_for_elements(wildcard_locator[0], self.random_wait_time(), silent=True)
        if not matched_links_elements:
            matched_links_elements = self.wait_for_elements(wildcard_locator[1], self.random_wait_time(), silent=True)
        matched_wildcard = self.matched_wildcard_click(matched_links_elements)
        if not matched_wildcard:
            self.save_page_html()
        return matched_wildcard
    
    def search_click_wildcard_base(self,wildcard_string,campaign_type=None):
        return super().search_click_wildcard(wildcard_string,campaign_type)
    
    def click_image_tab(self):
        image_tab = self.wait_for_element(GoogleSearchLocators.image_tab)
        if not image_tab:
            self.save_page_html()
            return False
        self.click(image_tab)
        return True    
    
    def click_location_popup(self):
        popup = self.wait_for_element(GoogleSearchLocators.popup_btn, self.random_wait_time(), silent=True)
        if popup:
            utilities.log_message("Popup found. Going to close it.")
            self.click(popup)
            utilities.random_sleep()
                        
    def click_cookies_popup(self):
        popup = self.wait_for_element(GoogleSearchLocators.cookies_popup_btn, 5, silent=True)
        if popup:
            utilities.log_message("Cookies Popup found. Going to close it.")
            self.click(popup)
            utilities.random_sleep()            
            
    def navigate_to_homepage(self, url):
        """
        Navigates to the homepage by clicking on the homepage link in the knowledge panel.

        Args:
            url (str): The URL of the homepage to navigate to.

        Returns:
            bool: True if the homepage link is found and clicked, False otherwise.
        """
        homepage_link_locator = GoogleSearchLocators.get_homepage_xpath(url)
        homepage_link_element = self.wait_for_element(homepage_link_locator)
        if homepage_link_element:
            self.click(homepage_link_element)
            return True
        return False
    
    
    def click_show_more_business(self):
        """
        Clicks the 'Show More Business' button if it is present on the page.

        Returns:
            bool: True if the button was found and clicked, False otherwise.
        """
        more_business_locator = self.wait_for_element(GoogleSearchLocators.show_more_business, timeout=self.random_wait_time())
        if not more_business_locator:
            return False
        self.click(more_business_locator)
        return True  