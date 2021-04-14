from selenium import webdriver
import  time

#初始化信息
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="10"
desired_caps["deviceName"]="HONOR30 Pro"
desired_caps["appPackage"]="com.huawei.calculator"
desired_caps["appActivity"]="com.huawei.Calculator"


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
# #在搜索框输入关键词
# driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
# 等待时间
time.sleep(3)
# driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("adidas")
# time.sleep(3)
# driver.find_element_by_id("com.taobao.taobao:id/searchbtn").click()
#截图
driver.quit()