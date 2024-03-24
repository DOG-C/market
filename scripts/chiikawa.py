from utilities import browser

from sites.chiikawa.pages.login import Login

class Chiikawa():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def run(self):
        driver = browser.get_chrome_driver()
        login = Login(driver)

        login.login(self.username, self.password)