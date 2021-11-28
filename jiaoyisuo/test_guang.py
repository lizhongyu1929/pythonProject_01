from selenium.webdriver.chrome import webdriver
from selenium import webdriver


class TestHogwards():
    def setup(self):       #setup指最先被调用的函数
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()   #窗口最大化
        self.driver.implicitly_wait(5)  #添加隐式等待；隐式等待只能查找到元素

    def teardown(self):    #teardown指最后被调用的函数
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("http://utr.gemas.com.cn/utr-web/flow/sendEmail.action")
        self.driver.find_element_by_id('userEname').send_keys('pjsun001')
        self.driver.find_element_by_id('upass').send_keys('pjsun001')
        self.driver.find_element_by_class_name('radius').click()
