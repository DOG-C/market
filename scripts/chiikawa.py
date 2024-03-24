from utilities import browser

from sites.chiikawa.pages.login import Login

class Chiikawa():

    def run(self):
        driver = browser.get_chrome_driver()
        login = Login(driver)

        login.login('caoyuqi1996@gmail.com', 'woshi6B19960613')