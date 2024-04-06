import time
from utilities import browser
from concurrent.futures import ThreadPoolExecutor
from sites.chiikawa.pages.login import Login
from sites.chiikawa.pages.cart import Cart
from sites.chiikawa.pages.product import Product

class Chiikawa():
    def __init__(self, username, password, header, path, keyword=None):
        self.username = username
        self.password = password
        self.header = header
        self.path = path
        self.keyword = keyword

    def open_link_in_new_tab(self, driver, link):
        """在新标签页中打开指定链接。"""
        driver.execute_script(f"window.open('{link}');")

    def operate_link_and_close(self, product, cart):
        product.driver.switch_to.window(product.driver.window_handles[1])
        # 在这里执行对链接的操作           
        if product.add_to_cart(cart):
            print("已添加")
        product.driver.close()


    def run(self):
        driver = browser.get_chrome_driver()
        login = Login(driver, self.header, self.path)

        login.login(self.username, self.password)
        new_items = login.go_to_new_items()

        if new_items.is_at_new_items():
            print("成功跳转到新着商品")
        else:
            print("跳转失败")
        
        links = new_items.go_to_product(self.keyword)

        with ThreadPoolExecutor(max_workers=len(links)) as executor:
            for link in links:
                executor.submit(self.open_link_in_new_tab, driver, link)

        product = Product(driver)
        cart = Cart(driver)
        while len(driver.window_handles) > 1:
            self.operate_link_and_close(product, cart)
        # 最开始的标签页保持打开状态
        print("所有商品已添加")

        driver.switch_to.window(driver.window_handles[0])
        cart.go_to_cart()
        cart.check_out()
        print('结账啦')

