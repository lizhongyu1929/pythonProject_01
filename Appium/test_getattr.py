import pytest
from selenium.webdriver.remote import webdriver
from appium import webdriver
from hamcrest import *

class TestGetAttr:
    # 初始化操作
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
        # 添加可以写中文的权限
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        # 启动打开app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # # 添加隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
    #定义一个方法

    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
        assert "search" in search_ele.get_attribute("resource-id")

    @pytest.mark.skip
    def test_assert(self):
        a = 10
        b = 20
        assert a < b

    def test_hamcrest(self):
        #equal_to指期望值的意思 例如：10 = 10 就对，10 =9 就不对
        # assert_that(10,equal_to(9),'这是一个提示')
        #close_to 指上下浮动的意思 例如：10 上下浮动 2
        # assert_that(10 , close_to(10,2))
        #contains_string 指包含的意思，例如下面的例子指  前面的字符串包含后面的字符串
        assert_that("contains some string",contains_string("string"))

