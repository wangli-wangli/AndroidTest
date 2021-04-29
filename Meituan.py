from appium import webdriver
from time import sleep
desired_caps ={
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001 device",
  "appPackage": "com.sankuai.meituan",
  "appActivity": ".city.CityActivity"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.launch_app()