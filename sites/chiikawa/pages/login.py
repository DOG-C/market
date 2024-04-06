# -*- coding: utf-8 -*-
import os, sys
import pickle
import requests
from utilities.explicit_wait import check_presence_of_element
from requests import session
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .new_items import NewItems

class Login:
    def __init__(self, driver, header, path):
        self.cookies_path = os.path.join(path, 'cookies_chiikawa.pkl')
        self.driver = driver
        self.login_cookies = {}
        self.session = session()
        # 登陆页面url和登陆页面的title
        self.login_site_info = ['https://chiikawamarket.jp/account/login', 'アカウント | ちいかわマーケット']
        # 成功登陆后的账号页面和账号页面title
        self.account_site_info = ['https://chiikawamarket.jp/account', 'アカウント | ちいかわマーケット']
        # 登陆相关的headers内容
        self.headers = header

        # 元素定位器
        self.username_locator = (By.ID, 'customer_email')
        self.password_locator = (By.ID, 'customer_password')
        self.login_button_locator = (By.CLASS_NAME, 'account--sign-in')

    def check_cookies_pkl(self):
        if os.path.exists(self.cookies_path):
            return True
        return False

    def save_cookies(self):
        with open(self.cookies_path, 'wb') as fw:
            pickle.dump(self.login_cookies, fw)

    def load_cookies_from_pkl(self):
        try:
            with open(self.cookies_path, 'rb') as fr:
                cookies = pickle.load(fr)
            self.login_cookies.update(cookies)
        except Exception as e:
            print('-' * 10, '加载cookies失败', '-' * 10)
            print(e)

    def get_cookies_from_driver(self):
        for cookie in self.driver.get_cookies():
            self.login_cookies[cookie['name']] = cookie['value']

    def check_login_status(self):
        response = requests.get(
            self.account_site_info[0],
            headers=self.headers,
            cookies=self.login_cookies
        )

        account_info =BeautifulSoup(response.text, "html.parser")
        if account_info.title.text == self.account_site_info[1]:
            return True
        else:
            return False
        
    def open(self):
        self.driver.get(self.login_site_info[0])

    def enter_username(self, username):
        username_input = self.driver.find_element(*self.username_locator)
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_locator)
        password_input.send_keys(password)
    
    def click_login_button(self):
        login_button = self.driver.find_element(*self.login_button_locator)
        login_button.click()

    def check_redirect(self):
        WebDriverWait(self.driver, 180, 0.5).until(EC.title_contains(self.login_site_info[1]))
        if self.driver.title != self.login_site_info[1]:
            print('登录异常，请检查页面登录提示信息')
            return False
        return True
    
    def go_to_new_items(self):
        self.driver.get("https://chiikawamarket.jp/collections/newitems")
        return NewItems(self.driver)

    def login(self, username, password):
        if not self.check_cookies_pkl():
            self.open()
            if check_presence_of_element(self.driver, self.username_locator):
                self.enter_username(username)
                self.enter_password(password)
                self.click_login_button()
            if self.check_redirect():
                self.get_cookies_from_driver()
        else:
            self.open()
            print('11111')
            self.load_cookies_from_pkl()
            for name, value in self.login_cookies.items():
                cookie = {'name': name, 'value': value}
                self.driver.add_cookie(cookie)
        
        login_status = self.check_login_status()
        if not login_status:
            print('-' * 10, '登录失败, 请检查登录账号信息。若使用保存的cookies, 则删除cookies文件重新尝试', '-' * 10)
            return
        elif login_status and not os.path.exists(self.cookies_path):
            self.save_cookies()