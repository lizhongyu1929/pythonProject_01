import time
from selenium_frame_window.base import Base
import pytest


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        #滑动到页面最底端
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="help"]/a[1]').click()
        #此处有疑问：元素定位不到
        # self.driver.find_element_by_xpath('//*[@id="page"]/div/a[11]').click()
        time.sleep(5)
        # for code in[
        #     'document.title','return JSON.stringify(performance.timing)'
        # ]:
        # print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))


    def test_datettime(self):
        #打开网址
        self.driver.get("https://www.12306.cn/index/")
        #用js去掉readonly属性
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        #输入日期文本
        self.driver.execute_script("document.getElementById('train_date').value='2021-12-30'")
        #强制等待3秒
        time.sleep(3)
        #打印发出日期后 return关闭网址
        print(self.driver.execute_script("return document.getElementById('train_date').value"))


