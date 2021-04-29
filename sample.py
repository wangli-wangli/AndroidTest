import time

from appium import webdriver
from time import sleep
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        desired_caps ={
          "platformName": "Android",
          "platformVersion": "7.1.2",
          "deviceName": "127.0.0.1:62001 device",
          "appPackage": "hxb.prepayment",
          "appActivity": "io.dcloud.PandoraEntryActivity"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
       # self.driver.launch_app()#Remote 时已经打开app了
        time.sleep(10)
        print('----------start-----------------')
    def tearDown(self):
        print('----------end---------------')
    def testLogin(self):
        el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View[2]")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.EditText")
        el2.send_keys("15176128570")
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.widget.EditText")
        el3.send_keys("000000")
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[8]/android.view.View[2]")
        el4.click()
        time.sleep(2)
        el5=self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View/android.view.View[1]')
        self.assertEqual(el5.text,"登录账户")

if __name__ == '__main__':
    unittest.main()



