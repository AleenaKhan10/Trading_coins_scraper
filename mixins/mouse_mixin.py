import time
import random

import numpy as np
import pyautogui
import mouse
from scipy.interpolate import interp1d
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from locators.locator_base_page import BasePageLocators
from common_components import constants, utilities

class MouseMovementMixin:
    """
    This mixin class provides methods for moving the mouse to specific locations.
    """
    def generate_random_curve(self, start_x, start_y, end_x, end_y, recursion_count=0):
        """
        This function generates a random cubic curve between two points.

        ## Parameters:
        - `start_x`: The x-coordinate of the starting point.
        - `start_y`: The y-coordinate of the starting point.
        - `end_x`: The x-coordinate of the ending point.
        - `end_y`: The y-coordinate of the ending point.
        - `recursion_count`: The count of recursion attempts.

        ## Returns:
        - A cubic curve function.
        """
        try:
            # Create array with random x points between start and end
            x_points = [start_x, end_x] + random.sample(range(min(start_x, end_x), max(start_x, end_x)), 5)
            x_points.sort()

            # Create array with random y points between start and end
            y_points = [start_y, end_y] + random.sample(range(min(start_y, end_y), max(start_y, end_y)), 5)
            y_points.sort()
            if start_x > end_x:
                x_points.reverse()
            if start_y > end_y:
                y_points.reverse()

            # Create a function based on these random points
            curve = interp1d(x_points, y_points, kind='cubic', fill_value="extrapolate")
            time.sleep(1)
        except:
            if recursion_count < 3:
                curve = self.generate_random_curve(start_x, start_y, end_x, end_y, recursion_count+1)
            else:
                return None

        return curve
    def generate_random_coordinates(self):
        """
        This method generates random coordinates within the browser window.

        Returns:
        - `end_x`: The x-coordinate of the randomly generated point.
        - `end_y`: The y-coordinate of the randomly generated point.
        """
        # Get the window size and position
        window_info = self.driver.get_window_rect()
        window_x = window_info['x']
        window_y = window_info['y']
        window_width = window_info['width']
        window_height = window_info['height']

        # Define the boundaries
        left_boundary = window_x
        right_boundary = window_x + window_width
        top_boundary = window_y
        bottom_boundary = window_y + window_height

        # Generate random coordinates within these boundaries
        end_x = random.randint(left_boundary, right_boundary)
        end_y = random.randint(top_boundary, bottom_boundary)

        return end_x, end_y

    def random_mouse_movement(self, movement_count=1, duration=5):
        """
        Moves the mouse pointer randomly around the screen.

        This method moves the mouse pointer in a human-like way: along a cubic curve 
        from the current position to a randomly determined location. 

        Parameters:
        - `movement_count` (int, optional): The number of times the mouse pointer should be moved, defaults to 1.
        - `duration` (float, optional): The time duration it takes for the mouse pointer to move to each new location, defaults to 0.5 seconds.

        Example:
            `random_mouse_movement(movement_count=3, duration=2) `
            The mouse pointer will be moved to three different locations on the screen over a duration of 2 seconds each.
        """

        for _ in range(movement_count):
            # Sleep for a random duration
            time.sleep(random.uniform(0.5, 1.5))

            # Generate random coordinates within the browser window
            end_x, end_y = self.generate_random_coordinates()

            start_x, start_y = pyautogui.position()

            self.move_mouse_to_coordinates(end_x, end_y, start_x, start_y)


    def move_mouse_to_coordinates(self, end_x: int, end_y: int, start_x, start_y):
        """
        # Move the mouse from the start coordinates to the end coordinates in a human-like way.
        The mouse movement is determined by a cubic curve.

        ## Parameters:
        - `end_x`: end x-coordinate
        - `end_y`: end y-coordinate
        - `duration`: duration of the movement
        """


        # Generate a random cubic curve between start and end points
        curve = self.generate_random_curve(start_x, start_y, end_x, end_y)
        if not curve:
            return
        x = np.linspace(start_x, end_x, num=100, endpoint=True)
        y = curve(x)

        # Loop over each point, moving the mouse to that location
        body = self.wait_for_element(BasePageLocators.body)
        
        for i in range(len(x)):
            
            # Moving the GUI mouse
            mouse.move(x[i], y[i])
            
            # Moving the selenium pointer
            try:
                self.driver.execute_script("""
                    arguments[0].dispatchEvent(new MouseEvent('mousemove', {'clientX': arguments[1], 'clientY': arguments[2]}));""",
                    body, x[i], y[i])
            except:
                pass
            
            start_y = y[i]
            start_x = x[i]

    def move_mouse_to_element(self, element: WebElement):
        """
        Move the mouse to a random location within a WebElement.

        Parameters:
        - `element`: a Selenium WebElement
        """
        try:
            # Get the size and location of the element
            loc = element.location
            size = element.size

            # Obtain the window position
            window_position = self.driver.get_window_position()

            # Calculate the height of the title and URL bar
            bars_height = self.driver.execute_script("return window.outerHeight - window.innerHeight")

            # Adjust the location of the WebElement by the position of the WebDriver's browser window
            loc['x'] += window_position['x']
            loc['y'] += window_position['y'] + bars_height

            # Get the position of each side of the element
            top, bottom = loc['y'], loc['y'] + size['height']
            left, right = loc['x'], loc['x'] + size['width']

            # Generate a random location within these bounds
            end_x = int(random.uniform(left, right))
            end_y = int(random.uniform(top, bottom))

            
            start_x, start_y = pyautogui.position()

            self.move_mouse_to_coordinates(end_x, end_y, start_x, start_y)

        except Exception as e:
            pass
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.perform()
        except:
            pass
        
    
    def move_mouse_to_captcha_element(self, element, x_iframe, y_iframe, top_height):
        """
        Move the mouse to a random location within a WebElement.

        Parameters:
        - `element`: a Selenium WebElement
        """
        try:
            # Get the size and location of the element
            loc = element.location
            size = element.size

            # Obtain the window position
            window_position = self.driver.get_window_position()

            # Adjust the location of the WebElement by the position of the WebDriver's browser window
            loc['x'] += window_position['x'] + x_iframe
            loc['y'] += window_position['y'] + top_height + y_iframe

            # Get the position of each side of the element
            top, bottom = loc['y'], loc['y'] + size['height']
            left, right = loc['x'], loc['x'] + size['width']

            # Generate a random location within these bounds
            end_x = int(random.uniform(left, right))
            end_y = int(random.uniform(top, bottom))

            pyautogui.moveTo(end_x, end_y, duration=0.5)
        except:
            pass
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.perform()
        except:
            pass
        
        
    def move_click_to_element(self, text):
        """
        Move the mouse to a random location within a WebElement.

        Parameters:
        - `element`: a Selenium WebElement
        """
        try:
            window_width = self.driver.execute_script("return window.innerWidth;")
            window_height = self.driver.execute_script("return window.innerHeight;")
            # Get the size and location of the element
            if self.driver.current_url == constants.URL_GOOGLE_SEARCH:

                loc = {'x': window_width/2, 'y': window_height/2}
                size = {'height': 20, 'width': 100}

            else:
                loc = {'x': window_width/2, 'y': 20}
                size = {'height': 20, 'width': 50}


                # Calculate the height of the title and URL bar
                bars_height = self.driver.execute_script("return window.outerHeight - window.innerHeight") 

                loc['y'] += bars_height 
                          
            window_position = self.driver.get_window_position()

            # Generate a random location within these bounds
            loc['x'] += window_position['x']
            loc['y'] += window_position['y']

            end_x = int(loc['x'])
            end_y = int(loc['y'])

            start_x, start_y = pyautogui.position()

            self.move_mouse_to_coordinates(end_x, end_y, start_x, start_y)

            actions = ActionChains(self.driver)

            self.driver.execute_script("window.onfocus")
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            for one in text:
                actions.send_keys(one).perform()
                utilities.random_sleep(0.05, 0.30)
            
        except Exception as e:
            pass
        
    def move_click_to_google_search(self, text):
        """
        Move the mouse to a random location within a WebElement.

        Parameters:
        - `element`: a Selenium WebElement
        """
        try:
            window_width = self.driver.execute_script("return window.innerWidth;")
            window_height = self.driver.execute_script("return window.innerHeight;")
            # Get the size and location of the element

            loc = {'x': window_width/2, 'y': 70}

                          
            window_position = self.driver.get_window_position()

            # Generate a random location within these bounds
            loc['x'] += window_position['x']
            loc['y'] += window_position['y']

            end_x = int(loc['x'])
            end_y = int(loc['y'])

            start_x, start_y = pyautogui.position()

            self.move_mouse_to_coordinates(end_x, end_y, start_x, start_y)

            actions = ActionChains(self.driver)

            self.driver.execute_script("window.onfocus")
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            time.sleep(2)
            for one in text:
                pyautogui.typewrite(one)
                utilities.random_sleep(0.05, 0.30)
            pyautogui.keyDown('enter')
            pyautogui.keyUp('enter')
        except Exception as e:
            pass