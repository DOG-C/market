from utilities import browser

from sites.chiikawa.pages.login import Login
from sites.chiikawa.pages.cart import Cart

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
        
        product = new_items.go_to_product(self.keyword)

        if product.add_to_cart():
            print('成功加入购物车')
            cart = Cart(driver)            

            if cart.is_at_cart():
                cart.check_out()
                print('结账啦')
            else:
                print('没有自动进入购物车')
        else:
            print('加入购物车失败')
