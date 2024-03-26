from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Product():
    def __init__(self, driver):
        self.driver = driver

        # 元素定位器
        self.checkbox_locator = (By.CSS_SELECTOR, "input#productAgree")
        self.add_to_cart_locator = (By.CSS_SELECTOR, "button.product-form--add-to-cart")

    def add_to_cart(self):
        try:
            # 等待位于agree_box div中的checkbox出现
            checkbox = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.checkbox_locator)
            )

            # 等待加入购物车按钮
            add_to_cart_button = self.driver.find_element(*self.add_to_cart_locator)

            while True:
                # 勾选注意事项
                if not checkbox.is_selected():
                    checkbox.click()

                # 如果按钮不是disabled，点击它
                if add_to_cart_button.get_attribute("disabled") is None:
                    add_to_cart_button.click()
                    return True
                else:
                    # 如果按钮是disabled，取消勾选
                    checkbox.click()

        except (NoSuchElementException, TimeoutException):
            # 如果找不到元素或者出现超时，刷新页面重新尝试
            self.driver.refresh()