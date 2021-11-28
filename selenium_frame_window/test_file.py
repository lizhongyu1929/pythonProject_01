

from selenium_frame_window.base import Base
from time import sleep

# class TestFile(Base):
#     def test_file_upload(self):
#         self.driver.get("https://image.baidu.com/")
#         self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
#         self.driver.find_elements_by_id("stfile").send_keys("F:\pythonProject_01\selenium_frame_window\img\1.png")
#         sleep(5)


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("F:\pythonProject_01\selenium_frame_window\img\1.png")
        sleep(5)