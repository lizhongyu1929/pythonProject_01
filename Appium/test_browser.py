from appium import webdriver
from time import sleep


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName':'android',
            'platformVersion':'10.2.0.108',
            'browserName':'Browser',
            'noReset': True,
            'deviceName':'QLXBBCA662110376',
            # 'chromedriverExecutable':'/Users/juanxu/Documents/chromedriver'
        }


        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        #添加隐式等待
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        # self.driver.get("http://m.baidu.com")
        self.driver.get("https://www.baidu.com/")
        sleep(5)