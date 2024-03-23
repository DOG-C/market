import re
import os
import json
import tools
import argparse
import requests
from requests import session

class ChiikawaMarket:
    def __init__(self):
        self.login_cookies = {}
        self.session = session()
        # 登陆页面url和登陆页面的title
        self.login_site_info = ['https://chiikawamarket.jp/account/login', 'アカウント | ちいかわマーケット']
        # 成功登陆后的账号页面和账号页面title
        self.account_site_info = ['https://chiikawamarket.jp/account', 'アカウント | ちいかわマーケット']
        # 登陆的账号
        self.login_id: str = 'caoyuqi1996@gmail.com'
        # 登陆的密码
        self.login_password: str = 'woshi6B19960613'
        # 登陆相关的headers内容
        self.headers = {
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
        'referer': 'chiikawamarket.jp',
        'accept-language': 'zh,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7',
        }
        
    def run(self):
        # 处理登陆信息，如果已有cookies就直接登陆，否则使用登陆信息进行第一次登陆
        if os.path.exists('cookies.pkl'):
            cookies = tools.load_cookies()
            self.login_cookies.update(cookies)
        elif 'account' == args.mode.lower():
            self.login_cookies = tools.account_login('account', self.headers, self.login_site_info, self.account_site_info, self.login_id, self.login_password)
        else:
            self.login_cookies = tools.account_login('qr')

        login_status = tools.check_login_status(self.login_cookies, self.headers, self.account_site_info)

        if not login_status:
            print('-' * 10, '登录失败, 请检查登录账号信息。若使用保存的cookies，则删除cookies文件重新尝试', '-' * 10)
            return
        elif login_status and not os.path.exists('cookies.pkl'):
            tools.save_cookies(self.login_cookies)

        # 正式处理商品部分

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--mode', type=str, default='account', required=False,
                        help='account: account login， QR: Scan QR code login')
    args = parser.parse_args()
    a = ChiikawaMarket()
    a.run()