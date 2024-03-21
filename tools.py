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

    headers = {

    }

def account_login(login_type: str, login_id=None, login_password=None):
    account_title = 'ちいかわマーケット-公式グッズショップ'

    headers = {
        'authority': 'chiikawamarket.jp',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://passport.damai.cn/login?ru=https://passport.damai.cn/accountinfo/myinfo',
        'accept-language': 'zh,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7',
    }

    response = requests.get(
        "https://chiikawamarket.jp/account",
        headers=headers,
        cookies=load_cookies
    )

    account_info =BeautifulSoup(response.text, "html.parser")
    if account_info.title.text == account_title:
        return True
    else:
        return False
