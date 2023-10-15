from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
# 配置Chrome无头选项
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# 初始化ChromeDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.baidu.com")
time.sleep(2)

# 获取页面标题
title = driver.title
print("Title:", title)
now_url = driver.current_url
print(now_url)
# 获取文本框对象
input_button = driver.find_element(By.ID, 'kw')
# print(input_button)
# 在文本框里面输入关键字
input_button.send_keys('IU')
time.sleep(2)
# 点击百度一下
input_button_bd = driver.find_element(By.ID, 'su')
input_button_bd.click()
time.sleep(2)

# 获取图片的文本链接
link = driver.find_element(By.XPATH, '//*[@id="s_tab"]/div/a[4]')
link1 = driver.find_element(By.XPATH, '//*[@id="3"]/div[1]/h3/a')
# print(link)
# print(link1)
link1.click()
time.sleep(2)

# 点击高清图片
link_picture = driver.find_element(By.NAME, 'pn0')
link_picture.click()
time.sleep(2)



# 防止网页关闭
num = input("是否结束：Y/N")
driver.quit()


