import time
import random
from selenium.webdriver.common.by import By
from utilities.explicit_wait import check_presence_of_element
from .product import Product

class NewItems():
    def __init__(self, driver):
        self.driver = driver
        self.title = "新着商品 | ちいかわマーケット" 

        # 元素定位器
        self.product_locator = (By.CSS_SELECTOR, "div.product--root")
        self.parent_locator = (By.CSS_SELECTOR, "div.collection--body--grid.collections_wrapper")

    def is_at_new_items(self):
        if self.driver.title == self.title:
            return True
        return False
    
    def find_links_with_keyword(self, keyword):
        # 初始化一个列表来存储找到的符合条件的hrefs
        found_hrefs = []
        
        while True:
            start_time = time.time()
            check_presence_of_element(self.driver, self.parent_locator)

            parent = self.driver.find_elements(*self.parent_locator)
            
            # 查找所有位于product_root div中的<a>标签
            product_roots = parent[0].find_elements(*self.product_locator)
            
            for product_root in product_roots:

                links = product_root.find_elements(By.TAG_NAME, "a")

                for link in links:
                    aria_label = link.get_attribute("aria-label")
                    if aria_label and keyword in aria_label:  # 确保aria-label不为空且包含关键词
                        href = link.get_attribute("href")
                        found_hrefs.append(href)
            
            # 检查是否找到了符合条件的链接
            if found_hrefs:
                # 记录查找所需时间
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"搜索时间：{elapsed_time}秒")

                # 如果找到了，退出循环
                break
            else:       
                # 如果没有找到，刷新页面再次尝试
                self.driver.refresh()
        
        return found_hrefs
            
    def go_to_product(self, keyword):
        found_links = self.find_links_with_keyword(keyword)
        selected_link = random.choice(found_links)
        self.driver.get(selected_link)

        return Product(self.driver)