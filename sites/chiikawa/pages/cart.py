from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.explicit_wait import check_presence_of_element

class Cart():
    def __init__(self, driver):
        self.driver = driver
        self.title = "ショッピングカート | ちいかわマーケット"

        # 元素定位器
        self.checkbox_locator = (By.CSS_SELECTOR, "input#termsCheck.termsCheck")
        self.checkout_locator = (By.NAME, "checkout")
    
    def is_at_cart(self):
        if self.driver.title == self.title:
            return True
        return False

    def check_out(self):
        checkbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.checkbox_locator)
            )

        checkout_button = self.driver.find_element(*self.checkout_locator)

        while True:
                # 勾选注意事项
                if not checkbox.is_selected():
                    checkbox.click()

                # 如果按钮不是disabled，点击它
                if checkout_button.get_attribute("disabled") is None:
                    checkout_button.click()
                    break
                else:
                    # 如果按钮是disabled，取消勾选
                    checkbox.click()