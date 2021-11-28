import pytest
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to
from selenium.webdriver.remote import webdriver
from appium import webdriver
class TestWebDriverWait:
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
        self.driver.implicitly_wait(8)

    def teardown(self):
        #点击取消操作
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        pass
    #设置参数化，编写多条测试用例
    @pytest.mark.parametrize('searchkey,type,expect_price',[
        ('alibaba','BABA',140),
        ('xiaomi','01810',20),
        ('tesila','TSLA',1135)
    ])
    def test_search(self,searchkey,type,expect_price):
        """
        1、打开雪球  应用
        2、点击 搜索框
        3、输入 搜索词 ’alibaba‘ or ’xiaomi‘
        4、点击第一个搜索结果
        5、
        :return:
        """
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/name').click()
        price_element = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        #把price_element 转成fioat类型
        current_price = float(price_element.text)
        # expect_price = 140
        print(f"当前的价格{current_price}")
        #设置断言
        assert_that(current_price,close_to(expect_price,expect_price*0.1))


