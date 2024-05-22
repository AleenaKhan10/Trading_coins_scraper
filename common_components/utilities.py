# Description: This file contains all the common functions that are used in the project
import time
import random
import os
import socket
import datetime
import uuid
import pytz
import logging
import requests
# import psutil
from urllib.parse import unquote_plus
from common_components import constants
import csv


def setup_logging():
    
    if not os.path.exists(constants.LOG_FOLDER):
        os.mkdir(constants.LOG_FOLDER)
        
    log_file_path = os.path.join(constants.LOG_FOLDER, 'log_file')
    
    logging.basicConfig(filename=log_file_path, filemode='a',
                        format='%(asctime)s - %(message)s', level=logging.INFO)


def log_message(message):
    """
        It will log the message in the log file
        Params:
            message (String)
    """
    print(message)
    logging.info(message)


def get_config_value(config_key, default_val):
    """
        Provides configuration settings from env variables
        Params:
            config_key (.env config key. String)
            default_val (value. String)
        Return:
            default_value (String)
    """
    if os.getenv(config_key):
        return os.getenv(config_key)
    else:
        return default_val


def random_sleep(min_sleep=1, max_sleep=3):
    """
        It stops the execution of code for specific amount of time
        Params:
            min_sleep (int)
            max_sleep (int)
    """
    random_wait = random.uniform(min_sleep, max_sleep)
    time.sleep(random_wait)
    return random_wait

def get_referral_url():
    return random.choice(constants.REFERRAL_URLS)

def get_random_value_from_list(user_list):
    """
        It will return the random value from the list.
        Params:
            user_list (List)
        Return:
            random_value (String)
    """
    random_value = random.choice(user_list)

    return random_value


def focus_browser(driver):
    driver.execute_script("""
        window.onblur = function () { 
            window.onfocus = function () { 
                window.focus(); 
            }; 
        };
    """)
            
def create_or_append_csv_listing(list):
    file_exists = False
    try:
        with open('data.csv', 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(list)
    except FileExistsError:
        file_exists = True
        
    if file_exists:
        with open('data.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(list)

