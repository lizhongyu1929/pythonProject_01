import time
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import assert_that,close_to

class TestDW():
    #初始化操作
    def setup(self):
        desired_caps = {}
        # 测试的手机操作系统
        desired_caps['platformName'] = 'Android'
        # 测试手机操作系统的版本
        desired_caps['platformVersion'] = '6.0'
        # 使用的手机类型或模拟器类型
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # 所运行的app包名
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # app运行的事件
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 记住弹窗
        desired_caps['noReset'] = 'true'
        # 启动App时不停止App
        # desired_caps['dontStopAppOnReset'] = 'true'
        # 跳过权限设置，提升用例进程
        desired_caps['skipDeviceInitialization'] = 'true'
        #添加可以写中文的权限
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard']='true'
        # 启动打开app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #添加隐式等待
        self.driver.implicitly_wait(5)

    #资源回收操作
    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        """
        1、打开 雪球App
        2、点击搜索输入框
        3、向搜索输入框里面输入"阿里巴巴"
        4、在搜索结果里面选择"阿里巴巴"，然后进行点击
        5、获取 阿里巴巴的股价，并判断 这只股价的价格>100
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        #进行断言
        assert current_price > 100


    def test_attr(self):
        """
        1、打开【雪球】应用首页
        2、定位首页的搜索框
        3、判断搜索框的是否可用，并查看搜索框name属性值
        4、打印搜索框这个元素的左上角坐标和它的宽高
        5、向搜索框输入：alibaba
        6、判断【阿里巴巴】是否可见
        7、如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        :return:
        """
        element = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        #查看搜索框方法
        search_enabled = element.is_enabled()
        #查看搜索框name属性值
        print(element.text)
        #查看搜索框坐标
        print(element.location)
        #查看搜索框的宽和高
        print(element.size)

        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']")
            #判断alibaba_element中的元素是否可见
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜素成功")
            else:
                print("搜索失败")
    #屏幕滑动操作
    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        #设备屏幕的宽
        width = window_rect['width']
        #设备屏幕的高
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x= x1,y=y_start ).wait(500).move_to(x=x1,y=y_end).release().perform()


    def test_get_current(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']").click()
        #定义一个locator
        locator = (By.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        #进行显示等待
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        #用lambda表达式进行显示等待
        # ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        ele = self.driver.find_element(*locator)
        print(ele.text)
        current_price = float(ele.text)

        # current_price = self.driver.find_element_by_xpath(locator).text
        print(f"当前09988 对应的股价价格是：{current_price}")
        expect_price = 170
        # assert float(current_price) > 100
        assert_that(current_price,close_to(expect_price,expect_price*0.1))

    def test_myinfo(self):
        """
        1、点击我的 ， 进入到个人信息页面
        2、点击登录，进入到登录页面
        3、输入用户名，输入密码
        4、点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("登录雪球")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12345")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("67890")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("热门")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("高岭的快乐").'
                                                        'instance(0));').click()
        time.sleep(5)


if __name__ == '__main__':
    pytest.main()