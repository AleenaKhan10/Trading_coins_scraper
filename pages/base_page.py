# Standard library imports
import os
import datetime
import logging
import random
import time
from pathlib import Path
from typing import List, Tuple, Optional, Union

# Third party imports
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, ElementNotInteractableException, StaleElementReferenceException, JavascriptException, WebDriverException

# Local application imports
from common_components import utilities,constants
from locators.locator_base_page import BasePageLocators
from mixins import AllMixin

pyautogui.FAILSAFE = False
class BasePage(AllMixin):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver: WebDriver) -> None:
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver


    def click(self, element: WebElement , x_iframe=None, y_iframe=None, top_height=None, action='normal') -> None:
        """ Performs click on web element whose locator is passed to it"""
        # element = self.wait_for_element(by_locator)
        
        try:
            if element.is_enabled() and element.is_displayed() and '/sorry/index?continue' in self.driver.current_url:
                self.move_mouse_to_captcha_element(element, x_iframe, y_iframe, top_height)
            else:
                self.move_mouse_to_element(element)
        except:
            pass
        try:
            element.click()
        except:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                element.click()
            except:
                try:
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    self.driver.execute_script("arguments[0].click();", element)
                except:
                    utilities.log_message("Unable to click on element")
    
    def click_random_element(self, by_locator: Tuple[str, str]) -> None:
        """ Performs click on a random web element whose locator is passed to it"""
        actions = ActionChains(self.driver)
        element = self.get_random_element(by_locator)
        actions.move_to_element(element)
        self.click(element)
    
    def create_folder(self, folder_path: str) -> None:
        """ Creates a folder if it does not already exist"""
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def save_page_html(self) -> None:
        """ Saves the HTML of the current page to a file"""
        try:
            filename = self.get_filename(".html")
            path = constants.BASE_DIR / constants.HTML_SAVE_FOLDER
            self.create_folder(path)
            file_path = path / filename
            html = self.driver.page_source
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
        except Exception as e:
            utilities.log_message(f"An error occurred while saving html")
            logging.exception(e)
    
    def get_random_element(self, by_locator: Tuple[str, str]) -> WebElement:
        """ Returns a random web element whose locator is passed to it"""
        elements = self.wait_for_elements(by_locator)
        element = random.choice(elements)
        return element
    
    def enter_text(self, by_locator: Tuple[str, str], text: str) -> None:
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        
        self.driver.execute_script("window.onfocus")
        element = self.wait_for_element(by_locator)
        if element:
            try:
                element.clear()
            except ElementNotInteractableException:
                utilities.log_message("Element is not interactable.")
            except StaleElementReferenceException:
                utilities.log_message("Stale element reference error occurred")
                
            self.move_mouse_to_element(element)
            for one in text:
                element.send_keys(one)
                utilities.random_sleep(0.05, 0.30)
        else:
            self.move_click_to_element(text)
            self.press_enter_on_element(by_locator)
    
    def wait_for_elements(self, locator: Tuple[str, str], timeout: int=constants.WAIT_TIMEOUT, silent=False) -> Optional[List[WebElement]]:
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return elements
        except TimeoutException:
            if not silent:
                logging.exception(f"Elements with locator {locator} on url {self.driver.current_url} not found within {timeout} seconds")
            return None
        
    def wait_for_element(self, locator: Tuple[str, str], timeout: int=constants.WAIT_TIMEOUT, silent=False) -> Optional[WebElement]:
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            if not silent:
                logging.exception(f"Element with locator {locator} on url {self.driver.current_url} not found within {timeout} seconds")
            return None

    def wait_for_page_to_load(self, timeout: int=constants.WAIT_TIMEOUT) -> None:
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except TimeoutException:
            logging.exception(f"Page not loaded within {timeout} seconds")
            self.driver.execute_script("window.stop();")

    def get_element_text(self, locator: Tuple[str, str]) -> Optional[str]:
        try:
            return self.wait_for_element(locator).text
        except NoSuchElementException:
            logging.exception(f"Element with locator {locator} not found")
            return None

    def get_element_attribute(self, locator: Tuple[str, str], attribute: str) -> Optional[str]:
        try:
            element = self.wait_for_element(locator)
            return element.get_attribute(attribute)
        except NoSuchElementException:
            logging.exception(f"Element with locator {locator} not found")
            return None

    def press_enter_on_element(self, locator: Tuple[str, str]):
        try:
            element = self.wait_for_element(locator, self.random_wait_time(), silent=True)
            if element:
                element.send_keys(Keys.ENTER)
            else:
                ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        except (NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException):
            logging.exception(f"Element with locator {locator} not found or not editable")
        except TimeoutException:
            utilities.log_message("Time Out Exception Occurred, moving on")
    
    def open(self, url: str) -> bool:
        """
        Opens a given URL in the browser.

        This function sets a page load timeout, then tries to open the URL. If the URL contains "consent.google.com",
        it waits for the 'agree' button to appear and clicks it. It then waits for the page to load.

        If a TimeoutException occurs, it logs a message and returns False.
        If a JavascriptException occurs, it tries to get the URL again and logs the exception, then returns False.

        :param url: The URL to open
        :return: True if the page was successfully opened, False otherwise
        """
        self.driver.set_page_load_timeout(constants.WAIT_TIMEOUT)
        url_check = BasePageLocators.extract_domain_and_path(url)
        
        for i in range(3):
            utilities.log_message(f'opening {url}: Try Count {i+1}')
            try:
                escaped_url = url.replace("'", "\\'")  # Escape single quotes in the URL to prevent Javascript errors
                
                try:
                    self.driver.execute_script(f"window.location.href = '{escaped_url}'")
                except WebDriverException as e:
                    utilities.log_message(f"WebDriverException: The inspected target navigated.")
                    self.driver.get(url)
                except Exception as e:
                    utilities.log_message(f"Unexpected error occurred : {e}")
                    self.driver.get(url)
                    
                if "consent.google.com" in self.driver.current_url:
                    btn_agree = self.wait_for_element(BasePageLocators.btn_agree_accept_all, self.random_wait_time())
                    self.click(btn_agree)
                self.wait_for_page_to_load()
                if url_check in self.driver.current_url:
                    return True

            except TimeoutException:
                utilities.log_message("Time Out Exception Occurred, moving on")

            except JavascriptException:
                try:
                    self.driver.get(url)
                    logging.exception(f"Javascript error occurred while opening URL: {url}")
                    if url in self.driver.current_url:
                        return True
                except:
                    continue
        return False
            
    def switch_to_new_tab(self) -> None:
        total_windows = len(self.driver.window_handles)

        if total_windows > 1:
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.close()
            utilities.random_sleep(2, 3)
            self.driver.switch_to.window(self.driver.window_handles[0])
    
    def scroll_to_bottom_of_page_directly(self) -> None:
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            utilities.log_message(f"Unable to do the scrolling due to {e}")           

    def scroll_to_the_page_end(self, min_time=35, max_time=45) -> None:
        """
        Scrolls the page to the end
        """
        start_time = time.time()
        while (round(time.time() - start_time)) < random.randint(min_time, max_time):
            scroll = random.randint(100, 300)
            scroll_to = f"window.scrollBy(0,{scroll})"
            try:
                self.driver.execute_script(scroll_to, "")
            except:
                pass
            try:
                self.random_mouse_movement(constants.MIN_COUNT)
            except TimeoutException:
                utilities.log_message("Timeout exception occured while random mouse movement")
            utilities.random_sleep(0.1, 1)
    
    def search_element_wait_for_elements(
            self, main_element: WebElement, locator: Tuple[str, str], timeout: int=constants.WAIT_TIMEOUT, silent=False
            ) -> Optional[List[WebElement]]:
        try:
            if main_element:
                elements = main_element.find_elements(*locator)
                return elements
            else:
                if not silent:
                    logging.warning(f"Main element with locator {main_element} is None. Cannot find elements.")
                return None
        except TimeoutException:
            # try:
            #     self.driver.save_screenshot("screenshot_search_div.png")
            # except:
            #     pass
            if not silent:
                logging.exception(f"Elements with locator {locator} not found within {timeout} seconds")
            return None

    def search_click_wildcard(self, wildcard_string: set, campaign_type: Optional[str]=None) -> bool:

        wildcard_locator = BasePageLocators.get_wildcard_searchable(wildcard_string)
        if campaign_type == constants.CAMPAIGN_TYPE_SQUIDOOSH_SHOPPING:
            matched_links_elements = self.wait_for_elements(wildcard_locator[0], self.random_wait_time(), silent=True)
            
        elif campaign_type == constants.CAMPAIGN_TYPE_TWO_STEP:
            
            current_url = self.driver.current_url
            
            matched_links_element = self.wait_for_elements(wildcard_locator[2], self.random_wait_time(), silent=True)
            if matched_links_element:
                for element in matched_links_element:
                    self.click(element)
                    self.random_wait_time()
                    try:
                        tab_count = len(self.driver.window_handles) 
                    except:
                        tab_count = 0
                                           
                    if tab_count > constants.TAB_COUNT or current_url != self.driver.current_url:
                        return True
                    
            wildcard_string = f"/{utilities.parse_product_wildcard(wildcard_string)}"
            wildcard_locator = BasePageLocators.get_wildcard_searchable(wildcard_string)
            
            matched_links_element = self.wait_for_element(wildcard_locator[2], self.random_wait_time(), silent=True)            
            if matched_links_element:
                self.click(matched_links_element)
                return True
        elif campaign_type == constants.CAMPAIGN_TYPE_ORGANIC_DIRECT:
            matched_links_element = self.wait_for_element(wildcard_locator[2], self.random_wait_time(), silent=True)
            if matched_links_element:
                self.click(matched_links_element)
                return True    
        else:
            if "google.com" in self.driver.current_url and 'google.com/maps' not in self.driver.current_url:
                search_div = self.wait_for_element(BasePageLocators.search_div)
                matched_links_elements = self.search_element_wait_for_elements(search_div, wildcard_locator, silent=True)
            else:
                matched_links_elements = self.wait_for_elements(wildcard_locator, self.random_wait_time(),  silent=True)
        
        try:
            matched_wildcard = self.matched_wildcard_click(matched_links_elements, constants.DEFAULT_IMAGE_NUMBER)
            if not matched_wildcard:
                self.save_page_html()

            return matched_wildcard
        except:
            return False
    
    def wildcard_interaction(self) -> None:
        try:
            self.switch_to_new_tab()
        except WebDriverException as e:
            utilities.log_message(f"Unable to switch to new tab")
        self.scroll_to_the_page_end()
        utilities.log_message(f"Current URL: {self.driver.current_url}")
    
    def save_screenshot_with_time(self,source: str='') -> None:
        try:
            current_time = utilities.get_current_date_time()
            self.driver.save_screenshot(f"{source}_screenshot_{current_time}.png")
        except:
            pass

    def switch_to_frame(self, locator: Tuple[str, str], timeout: int=constants.WAIT_TIMEOUT) -> None:
        WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def random_wait_time(self):
        return random.uniform(5, 8)
    
    def get_random_count(self, start_limit = constants.MIN_COUNT, end_limit = constants.MAX_COUNT ):
        return random.randint(start_limit, end_limit)
    
    def click_add_to_cart(self) -> None:
        add_to_cart_locator = self.wait_for_element(BasePageLocators.add_to_cart, self.random_wait_time(), silent=True)
        if add_to_cart_locator:
            self.click(add_to_cart_locator)
            
    def matched_wildcard_click(self, matched_links_elements: List[WebElement], image_number: int = 1) -> bool:
        """
        Clicks on the matched link element based on the provided image number.

        Args:
            matched_links_elements (List[WebElement]): List of matched link elements.
            image_number (int, optional): The index of the image to be clicked. Defaults to constants.DEFAULT_IMAGE_NUMBER.

        Returns:
            bool: True if the click action is successful, False otherwise.
        """
        # Check if the list of matched link elements is not empty
        if matched_links_elements:
            try:
                # Get the element to be clicked based on the image number
                element_matched = matched_links_elements[image_number-1]
                
                # Perform the click action
                self.click(element_matched)
                
                # Return True if the click action is successful
                return True
            except IndexError:
                # Log a message if the image number is out of range
                utilities.log_message("Image Index is out of range.")
                element_matched = matched_links_elements[0]
                self.click(element_matched)
                utilities.log_message("Going to click first image.")
                if element_matched:
                    return True
            except ElementNotInteractableException:
                utilities.log_message("Element is not interactable.")
            except StaleElementReferenceException:
                utilities.log_message("Element is no longer attached to the DOM.")
            except NoSuchElementException:
                utilities.log_message("Element does not exist on the page.")
        
        # Return False if the list of matched link elements is empty or the image number is out of range
        return False

