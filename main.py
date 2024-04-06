import os, sys
import json
from scripts import chiikawa

if __name__ == '__main__':
    path = os.path.dirname(__file__)
    # 导入抢购信息
    setup_path = os.path.join(path, 'setup.json')
    with open(setup_path, 'r') as file:
        info = json.load(file)
    username = info['username']
    password = info['password']
    header = info['header']
    keyword = info['keyword']
    a = chiikawa.Chiikawa(username, password, header, path, keyword)
    a.run()