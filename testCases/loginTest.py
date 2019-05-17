import unittest, HtmlTestRunner, time
from selenium import webdriver
import sys
sys.path.append(r"D:\PYTHON\PythonProjects\PythonUnitTestProject_POMBased")
from pageObjects.loginPage import LoginPage

class LoginTest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username =  "admin@yourstore.com "
    password = "admin"
    driver = webdriver.Chrome(executable_path="..\\drivers\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)

        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "webpage title not matched")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\reports"))