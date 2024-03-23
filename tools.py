import re
import os
import json
import execjs
import pickle
import platform
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def save_cookies(login_cookies):
    with open('cookies.pkl', 'wb') as fw:
        pickle.dump(login_cookies, fw)

def load_cookies():
    try:
        with open('cookies.pkl', 'rb') as fr:
            cookies = pickle.load(fr)
        return cookies
    except Exception as e:
        print('-' * 10, '加载cookies失败', '-' * 10)
        print(e)

def check_login_status(login_cookies, headers, account_site_info):
    account_url = account_site_info[0]
    account_title = account_site_info[1]

    response = requests.get(
        account_url,
        headers=headers,
        cookies=login_cookies
    )

    account_info =BeautifulSoup(response.text, "html.parser")
    if account_info.title.text == account_title:
        return True
    else:
        return False

def check_id_of_element(driver, element):
    try:
        # 使用 WebDriverWait 等待页面加载完成
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, element))
        )
        return True
    except TimeoutException:
        return False
    
def find_shadow_dom_element(driver, host, element):
    shadow_element = driver.execute_script("""
                const hostElement = document.getElementById(arguments[0]);
                const shadowRoot = hostElement.shadowRoot;
                const shadowElement = shadowRoot.querySelector(arguments[1]);
                return shadowElement;
        """, host, element)
    return shadow_element

def handle_with_shadow_dom(driver, host, element, operator, input=None):
    if operator == 'click':
        shadow_element = find_shadow_dom_element(driver, host, element)
        driver.execute_script("arguments[0].click();", shadow_element)

def account_login(login_type: str, headers: dict, login_site_info: list, account_site_info: list, login_id=None, login_password=None):
    login_url = login_site_info[0]
    loggedin_title = login_site_info[1]

    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
   # driver.set_page_load_timeout(60)
    
    driver.get(login_url)

    if login_type == 'account':
        # # 海外版本才需要的部分，关闭World Shopping窗口未实现
        # if check_id_of_element(driver ,"zigzag-worldshopping-checkout"):
        #     # 使用 JavaScript 来访问 Shadow DOM 并点击 "接受所有 Cookie" 按钮
        #     handle_with_shadow_dom(driver, 'zigzag-worldshopping-checkout', '#zigzag-test__cookie-banner-accept-all', 'click')
        
        if check_id_of_element(driver, 'customer_email'):
            driver.find_element(By.ID, 'customer_email').send_keys(login_id)
            driver.find_element(By.ID, 'customer_password').send_keys(login_password)
            driver.find_element(By.CLASS_NAME, 'account--sign-in').click()
    WebDriverWait(driver, 180, 0.5).until(EC.title_contains(loggedin_title))

    login_cookies = {}
    if driver.title != loggedin_title:
        print('登录异常，请检查页面登录提示信息')
    for cookie in driver.get_cookies():
        login_cookies[cookie['name']] = cookie['value']
    if check_login_status(login_cookies, headers, account_site_info):
        return login_cookies
    
