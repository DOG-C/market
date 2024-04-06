# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option("detach", True)
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.page_load_strategy = 'none'

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    return driver

def get_headless_chrome_driver():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.page_load_strategy = 'none'
    option.add_argument("--headless")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    return driver