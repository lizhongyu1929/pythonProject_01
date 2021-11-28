import time

from appium import webdriver

desired_caps={}
#测试的手机操作系统
desired_caps['platformName']='Android'
#测试手机操作系统的版本
desired_caps['platformVersion']='6.0'
#使用的手机类型或模拟器类型
desired_caps['deviceName']='127.0.0.1:7555'
#所运行的app包名
desired_caps['appPackage']='com.xueqiu.android'
#app运行的事件
desired_caps['appActivity']='com.xueqiu.android.common.MainActivity'
#记住弹窗
desired_caps['noReset']= 'true'
#启动App时不停止App
desired_caps['dontStopAppOnReset']= 'true'
#跳过权限设置，提升用例进程
desired_caps['skipDeviceInitialization']='true'
#启动打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#添加隐式等待
driver.implicitly_wait(5)
driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')

#返回到上一个页面
driver.back()
driver.back()
driver.quit()