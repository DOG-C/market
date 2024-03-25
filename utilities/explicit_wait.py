from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def check_presence_of_element(driver, element):
        try:
            # 使用 WebDriverWait 等待页面加载完成
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(element)
            )
            return True
        except TimeoutException:
            return False