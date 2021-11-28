from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

#填写注册信息
class Register:
    def __init__(self, driver:WebDriver):
        self._driver = driver
    def register(self):
        #send content
        #click element
        #corp_name
        sleep(2)
        self._driver.find_element(By.ID,'corp_name').send_keys("weddff")
        self._driver.find_element(By.ID,'manager_name').send_keys("box")
        sleep(5)
        self._driver.quit()
        return True
