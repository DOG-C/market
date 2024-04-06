# -*- coding: utf-8 -*-
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class Product():
    def __init__(self, driver):
        self.driver = driver
        
        # 元素定位器
        self.checkbox_locator = (By.CSS_SELECTOR, "input#productAgree")
        self.add_to_cart_locator = (By.CSS_SELECTOR, "button.product-form--add-to-cart")

    def add_to_cart(self, cart):
        try:
            # 设定循环运行的最大时长（秒）
            max_duration = 8

            # 等待位于agree_box div中的checkbox出现
            checkbox = WebDriverWait(self.driver, 6).until(
                EC.element_to_be_clickable(self.checkbox_locator)
            )

            add_to_cart_button = self.driver.find_element(*self.add_to_cart_locator)

            start_time = time.time()
            while time.time() - start_time < max_duration:
                # 勾选注意事项
                if not checkbox.is_selected():
                    checkbox.click()

                # 如果按钮不是disabled，点击它
                if add_to_cart_button.get_attribute("disabled") is None:
                    add_to_cart_button.click()
                    while cart.is_at_cart():
                        return True
                else:
                    # 如果按钮是disabled，取消勾选
                    checkbox.click()

        except WebDriverException:
            # 如果找不到元素或者出现超时，刷新页面重新尝试
            return False