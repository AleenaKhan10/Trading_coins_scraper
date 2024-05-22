from common_components import utilities, constants
from drivers.mlx_connection import get_mlx_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.google_search_page import GoogleSearchPage
from locators.locator_coins import CoinsLocator
from locators.locator_google_search import GoogleSearchLocators
import time
import pyautogui




# def google_search_with_random_url(driver):
#     google_search_page = GoogleSearchPage(driver)
#     google_search_page.open(constants.URL_GOOGLE_SEARCH)
#     utilities.random_sleep()
    
#     keyword = utilities.get_random_value_from_list(constants.TRENDING_COINS_KEYWORDS)
    
#     utilities.log_message(f"Searching for this kerword '{keyword}' on this URL '{driver.current_url}'")
#     google_search_page.search_keyword(keyword, constants.URL_GOOGLE_SEARCH)
    
#     google_search_page.click_location_popup()
#     google_search_page.scroll_to_the_page_end()
#     links = driver.wait_for_elements(GoogleSearchLocators.links_locator)
    
#     random_link = utilities.get_random_value_from_list(links)
    
#     google_search_page.click(random_link)
#     google_search_page.scroll_to_the_page_end()
    
#     referral_url = utilities.get_referral_url()        
#     utilities.log_message(f"refferal url : {referral_url}")
    
#     google_search_page.open(referral_url)
#     google_search_page.scroll_to_the_page_end()
    
    
def google_search_with_interaction(driver):
    google_search_page = GoogleSearchPage(driver)
    google_search_page.open(constants.URL_GOOGLE_SEARCH)
    utilities.random_sleep()
    
    keyword = utilities.get_random_value_from_list(constants.TRENDING_COINS_KEYWORDS)
    
    utilities.log_message(f"Searching for this kerword '{keyword}' on this URL '{driver.current_url}'")
    google_search_page.search_keyword(keyword, constants.URL_GOOGLE_SEARCH)
    
    google_search_page.click_location_popup()
    google_search_page.scroll_to_the_page_end()
    
    # referral_url = utilities.get_referral_url()        
    # utilities.log_message(f"refferal url : {referral_url}")
    
    # google_search_page.open(referral_url)
    # google_search_page.scroll_to_the_page_end()
    
    
def open_site_to_scrape(driver):
    
    # interactions = [google_search_with_random_url, google_search_with_interaction]
    # random_inc = utilities.get_random_value_from_list(interactions)
    
    # random_inc(driver)
    # google_search_with_interaction(driver)
    
    google_search_page = GoogleSearchPage(driver)
    google_search_page.open(constants.URL_GOOGLE_SEARCH)
    utilities.random_sleep()
    
    keyword = "birdeye coins"
    
    utilities.log_message(f"Searching for this kerword '{keyword}' on this URL '{driver.current_url}'")
    google_search_page.search_keyword(keyword, constants.URL_GOOGLE_SEARCH)
    
    google_search_page.search_click_wildcard("https://birdeye.so/find-gems?chain=solana")
    
    # solana_tab_locator = google_search_page.wait_for_element(CoinsLocator.solana_tab)
    # google_search_page.click(solana_tab_locator)
    
    
    # gems = google_search_page.wait_for_element(CoinsLocator.gems_locator)
    # google_search_page.click(gems)
    # time.sleep(10)
    # driver.execute_script("window.open('about:blank','_blank');")
    # last_tab = driver.window_handles[-1]
    # driver.switch_to.window(last_tab)
    
    # driver.get("https://birdeye.so/find-gems?chain=solana")
    # for _ in range(5):
    iframe_element = google_search_page.wait_for_element(CoinsLocator.iframe)
    driver.switch_to.frame(iframe_element)
    
    captcha_element = google_search_page.wait_for_element(CoinsLocator.captcha)
    google_search_page.click(captcha_element)
    time.sleep(10)
    driver.switch_to.default_content()
    time.sleep(10)
        
        # pyautogui.hotkey('ctrl', 't') 
        # last_tab = driver.window_handles[-1]
        # driver.switch_to.window(last_tab)
        # driver.get("https://birdeye.so/find-gems?chain=solana") 
        # time.sleep(5)
        # driver.switch_to.window(driver.window_handles[0]) 
        
        
        # headers = google_search_page.wait_for_elements(CoinsLocator.headers_locator, timeout=3)
        # if headers:
        #     break
        
        # solana_tab_locator = google_search_page.wait_for_element(CoinsLocator.solana_tab)
        # google_search_page.click(solana_tab_locator)
        # driver.switch_to.default_content()
        # gems = google_search_page.wait_for_element(CoinsLocator.gems_locator)
        # google_search_page.click(gems)
    
    
    
    

def extract_headers_and_create_csv(driver):
    google_search_page = GoogleSearchPage(driver)
    
    try:
        
        headers = google_search_page.wait_for_elements(CoinsLocator.headers_locator)
        
        header_texts = [header.text for header in headers if header.text]
        
        utilities.create_or_append_csv_listing(header_texts)
        
    except Exception as e:
        print(f"An error occurred: {e}")



def extract_rows_and_update_csv(driver, count):
    google_search_page = GoogleSearchPage(driver)
    for _ in range(count):
        try:
            time.sleep(10)
            rows = google_search_page.wait_for_elements(CoinsLocator.rows_locator)
            
            for row in rows:
                try:
                    data = []
                    cells = row.find_elements(By.XPATH, './td')
                    for index, cell in enumerate(cells):
                        try:
                            if index == 1:  # Special handling for the second cell
                                anchor_tag = cell.find_element(By.TAG_NAME, 'a').get_attribute('href')
                                cell_data = f"{cell.text} ({anchor_tag})"
                            else:
                                cell_data = cell.text
                            if cell_data:
                                data.append(cell_data)
                        except:
                            cell_data = None
                            
                    utilities.create_or_append_csv_listing(data)        
                except:
                    pass
            
        except Exception as e:
            print(f"An error occurred while extracting rows: {e}")


        next_pg_btn = google_search_page.wait_for_element(CoinsLocator.next_pg_btn_locator)
        next_pg_btn.click()
        
def main():
    driver = get_mlx_driver()
    open_site_to_scrape(driver)
    extract_headers_and_create_csv(driver)
    page_count = 5
    extract_rows_and_update_csv(driver, page_count)

if __name__ == "__main__":
    
    main()
