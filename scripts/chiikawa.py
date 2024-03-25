from utilities import browser

from sites.chiikawa.pages.login import Login

class Chiikawa():
    def __init__(self, username, password, keyword=None):
        self.username = username
        self.password = password
        self.keyword = keyword

    def run(self):
        driver = browser.get_chrome_driver()
        login = Login(driver)

        login.login(self.username, self.password)
        new_items = login.go_to_new_items()

        if new_items.is_at_new_items():
            print("成功跳转到新着商品")
        else:
            print("跳转失败")
        
        