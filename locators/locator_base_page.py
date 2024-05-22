from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from common_components import constants

class BasePageLocators:
    @classmethod
    def get_wildcard_searchable(cls, wildcard_string):
        if wildcard_string == '':
            wildcard_string = None
        
        wildcard_string = cls.extract_domain_and_path(wildcard_string)
        
        if wildcard_string.startswith('www.'):
            wildcard_string = wildcard_string[4:]
            
        wildcard_string_all = constants.WILDCARD_STRING.format(wildcard_string)
        wildcard_match_string_search = constants.WILDCARD_STRING_SEARCH.format(wildcard_string)
        wildcard_match_string_botstuff = constants.WILDCARD_STRING_BOTSTUFF.format(wildcard_string)
        return [(By.XPATH, wildcard_match_string_search), (By.XPATH, wildcard_match_string_botstuff), (By.XPATH, wildcard_string_all)]
    
    @staticmethod
    def extract_domain_and_path(url):
        if url:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            path = parsed_url.path

            # Remove 'www.' if present
            if domain.startswith('www.'):
                domain = domain[4:]                
            elif domain.startswith('ww.'):
                domain = domain[3:]
            elif domain.startswith('w.'):
                domain = domain[2:]
                
            new_url =  f"{domain}{path}"

            if new_url.endswith('/'):
                new_url = new_url[:-1]
            return new_url
        
    @staticmethod
    def extract_domain(url):
        if url:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            path = parsed_url.path

            # Remove 'www.' if present
            if domain.startswith('www.'):
                domain = domain[4:]                
            elif domain.startswith('ww.'):
                domain = domain[3:]
            elif domain.startswith('w.'):
                domain = domain[2:]
                
            new_url =  f"{domain}"
            if domain == '':
                new_url =  f"{path}"

            if new_url.endswith('/'):
                new_url = new_url[:-1]
            return new_url

    search_div = (By.ID, "search")
    btn_agree_accept_all = (By.CSS_SELECTOR,"button[aria-label='Accept all']")
    body = (By.CSS_SELECTOR, 'body')
    add_to_cart = (By.XPATH, '//button[text()="Add to cart"] | //input[@value="Add to Cart"]')