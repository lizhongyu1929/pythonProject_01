from selenium import webdriver
from time import sleep
class TestHogwards():
    def setup(self):       #setup指最先被调用的函数
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()   #窗口最大化
        self.driver.implicitly_wait(5)  #添加隐式等待；隐式等待只能查找到元素

    def teardown(self):    #teardown指最后被调用的函数
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_css_selector(".topic-29703 .title > a").click()



