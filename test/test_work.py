from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup_method(self,method):
        options = Options()
        options.debugger_address = "127.0.0.1:10002"
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self,method):
        self.driver.quit()

    def test_demo(self):

        # self.driver.get("https://www.baidu.com/")
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_id("menu_contacts").click()
        print(self.driver.get_cookies())
        sleep(5)