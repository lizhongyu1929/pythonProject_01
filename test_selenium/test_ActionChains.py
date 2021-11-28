from selenium import webdriver
class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()


    def teardown(self):
        self.driver

    def test_case_click(self):
        pass