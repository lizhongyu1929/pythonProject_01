import shelve
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup_method(self,method):
        options = Options()
        options.debugger_address = "127.0.0.1:10002"
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_demo(self):

        # self.driver.get("https://www.baidu.com/")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_id("menu_contacts").click()
        # print(self.driver.get_cookies())

        db = shelve.open("cookies")
        #把数据的信息缓存到cookies文件里
        # db['cookie'] = self.driver.get_cookies()
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(5)
        db.close()
