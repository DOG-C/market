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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_cookies(login_cookies):
    with open('cookies.pkl', 'wb') as fw:
        pickle.dump(login_cookies, fw)

def load_cookies():
    """ 读取保存的cookies """
    try:
        with open('cookies.pkl', 'rb') as fr:
            cookies = pickle.load(fr)
        return cookies
    except Exception as e:
        print('-' * 10, '加载cookies失败', '-' * 10)
        print(e)

def check_login_status(login_cookies):
    login_title = 'アカウント | ちいかわマーケット'

def account_login(login_type: str, login_id=None, login_password=None):
    title = 'ちいかわマーケット-公式グッズショップ'
