
class NewItems():
    def __init__(self, driver):
        self.driver = driver
        self.title = "新着商品 | ちいかわマーケット"
    

    def is_at_new_items(self):
        if self.driver.title == self.title:
            return True
        return False