from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

import json
import logging
import requests
import hashlib



from common_components import constants, utilities
class MLXBrowser:

    def __init__(self):
        self.browser_profile_id = None
        self.host_port_driver = None
        self.token = None
        self.driver = None

    def sign_in(self):
        payload = {
            constants.MLX_EMAIL_FIELD: "aleenakhanraees40@gmail.com",
            constants.MLX_PASSWORD_FIELD: hashlib.md5("AleenaKhan_0786*".encode()).hexdigest()
            }
        
        
        
        url = constants.MLX_SIGNIN_URL.format(mlx_base = constants.MLX_BASE)

        r = requests.post(url, json=payload)

        if(r.status_code != 200):
            print(f'Error during login: {r.text}')

        response = r.json()[constants.MLX_DATA]

        token = response[constants.MLX_TOKEN]

        return token
    
    
    def open_browser(self):
        """
        It opens browser profile
        Params:
            self (object)
            one_query (dict)
        Return:
            host_port_driver
        """
        self.token = self.sign_in()
        profile_launcher_url = constants.MLX_LAUNCHER
        url = profile_launcher_url + constants.MLX_START_PROFILE_URL.format(
            folder_id = "1b5aad0b-c179-45cb-bb11-defde2826b43",
            profile_id = "56a87e20-51b5-4471-93a4-c0acc2db7c8d"
            )

        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f'Bearer {self.token}'
        }

        r = requests.get(url, headers=headers)

        response = r.json()

        if(r.status_code != 200):
            print(f'Error while starting profile: {r.text}')
        else:
            print(f'Profile {self.browser_profile_id} started.')

        return response
    

    def connect_browser(self, response):
        """
        It remotely connects browser
        Params:
            self (object)
        Return:
            driver (Selenium webdriver object)
        """
        selenium_port = response.get('status').get('message')
        options = ChromiumOptions()
        driver = webdriver.Remote(command_executor=f'{constants.LOCALHOST}:{selenium_port}', options=options)
        driver.maximize_window()

        return driver
    
    
    def multilogin_browser(self):
        browser_response = self.open_browser()
        self.driver = self.connect_browser(browser_response)
        return self.driver



def get_mlx_driver():
    driver = None
    mlx_browser = MLXBrowser()
    try:
        driver = mlx_browser.multilogin_browser()
    except Exception as e:
        print(f"got exception while connecting to browser {e}")
    return driver
