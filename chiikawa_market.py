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
        self.login_info = ['https://chiikawamarket.jp/account/login', 'アカウント | ちいかわマーケット']
        self.login_id: str = 'caoyuqi1996@gmail.com'
        self.login_password: str = 'woshi6B19960613'
        
       # self.item_id: int = 610820299671  # 商品id
       # self.viewer: list = ['viewer1']  # 在大麦网已填写的观影人
       # self.buy_nums: int = 1  # 购买影票数量, 需与观影人数量一致
       # self.ticket_price: int = 180  # 购买指定票价
        
    def run(self):
        if os.path.exists('cookies.pkl'):
            cookies = tools.load_cookies()
            self.login_cookies.update(cookies)
        elif 'account' == args.mode.lower():
            self.login_cookies = tools.account_login('account', self.login_info, self.login_id, self.login_password)
        else:
            self.login_cookies = tools.account_login('qr')

        login_status = tools.check_login_status(self.login_cookies)

        if not login_status:
            print('-' * 10, '登录失败, 请检查登录账号信息。若使用保存的cookies，则删除cookies文件重新尝试', '-' * 10)
            return
        elif login_status and not os.path.exists('cookies.pkl'):
            tools.save_cookies(self.login_cookies)

        #commodity_param, ex_params = tools.get_api_param()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--mode', type=str, default='account', required=False,
                        help='account: account login， QR: Scan QR code login')
    args = parser.parse_args()
    a = ChiikawaMarket()
    a.run()