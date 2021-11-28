from selenium import webdriver

from selenium_frame_window.base import Base
from time import sleep

class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        #打印窗口
        print(self.driver.current_window_handle)
        #打印当前所有窗口的名字
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        #打印窗口
        print(self.driver.current_window_handle)
        #打印当前所有窗口的名字
        print(self.driver.window_handles)
        #定义一个windows值

        windows = self.driver.window_handles
        #切换窗口，[-1]指切换到最后一个窗口
        self.driver.switch_to_window(windows[-1])
        # self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div/div/div/div/div/div[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys("123456789")
        sleep(5)
        #切换窗口，[0]指切换到第一个窗口
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__changePwdCodeItem"]').click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys("88888888")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
        sleep(5)


