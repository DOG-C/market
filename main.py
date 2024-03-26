from scripts import chiikawa

if __name__ == '__main__':
    # 抢购信息
    username = 'caoyuqi1996@gmail.com'
    password =  'woshi6B19960613'
    keyword = '東京みやげ お座りぬいぐるみ'
    a = chiikawa.Chiikawa(username, password, keyword)
    a.run()