from appium import webdriver
import time
desired_caps={}
desired_caps['platformName']='Android' #或者IOS
desired_caps['deviceName']='HONOR30 Pro' #手机设备名或者型号
desired_caps['platformVersion']='10' #安卓系统版本
desired_caps['appPackage']='com.android.permissioncontroller'
desired_caps['appActivity']='com.android.packageinstaller.permission.ui.GrantPermissionsActivity'
desired_caps['noReset']='True' #每次打开不重置
desired_caps['automationName']='uiautomator2'
#同时连接模拟器和真机时，必须有udid,里边的值写真机的adb devices
#desired_caps['udid']='d32ec644'
#如果手机还未安装APP，则需要写入路径
#desired_caps['app']=r'C:\Users\admin\Desktop\kaoyan3.1.0.apk'

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(2)
driver.quit()

