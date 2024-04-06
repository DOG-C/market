# -*- coding: utf-8 -*-
import os, sys
import json
from scripts import chiikawa

if __name__ == '__main__':
    # 如果是直接跑代码
    # path = os.path.dirname(__file__)

    # 如果是可执行文件（主要用于打包）
    path = os.path.dirname(os.path.realpath(sys.executable))

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