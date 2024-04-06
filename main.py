import os, sys
import json
from scripts import chiikawa

if __name__ == '__main__':

    # 导入抢购信息
    with open('setup.json', 'r') as file:
        info = json.load(file)
    username = info['username']
    password = info['password']
    header = info['header']
    keyword = info['keyword']
    a = chiikawa.Chiikawa(username, password, header, keyword)
    a.run()