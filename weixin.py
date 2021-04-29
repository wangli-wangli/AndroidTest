import time

from appium import webdriver
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        caps = {
            "platformName": "Android",  # 设备名称
            "deviceName": "84041a88",  # 设备号（通过adb命令工具查看）
            'newCommandTimeout': 6000,  # 设置命令超时时间
            'noReset': True,  # 确保自动化之后不重置app
            'automationName': 'UiAutomator2',  # 低层驱动
            # 查看webviwe版本方式2：通过代码的报错来查看
            # 指定chromedriver路径
            'chromedriverExecutable': r'C:\Program Files (x86)\Google\Chrome\Application\chromedriveradb .exe',
            # 指定小程序的进程（通过adb工具进行查看）
            'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},#com.tencent.mm com.miui.home
            'appActivity': '.ui.LauncherUI',  # 页面名称
            'appPackage': 'com.tencent.mm', }  # 包名
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
       # self.driver.launch_app()#Remote 时已经打开app了
        time.sleep(10)
        print('----------start-----------------')

    def tearDown(self):
        print('----------end---------------')

    def testLogin(self):
        print(self.driver.window_handles)
        #self.driver.switch_to_window(self.driver.window_handles[1])
        #print(self.driver.current_window_handle)
        #print('----------------working--------------')
if __name__ == '__main__':
    unittest.main()
