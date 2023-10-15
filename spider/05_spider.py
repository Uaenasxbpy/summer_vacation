from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 创建一个无头浏览器实例，并配置一些选项。在这里，我们将使用headless选项来在后台运行浏览器，并禁用GUI
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
# 加载网页并提取标题
url = "https://www.baidu.com"
driver.get(url)
title = driver.title
print(title)

# 递归爬取所有内链
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    # 打开链接并获取页面信息
    driver.get(link.get_attribute("href"))
    # 获取标题
    title = driver.title
    # 打印
    print(title)

# # 定位表单元素并填充字段
# element = driver.find_element_by_id("username")
# element.send_keys("myusername")
#
# element = driver.find_element_by_id("password")
# element.send_keys("mypassword")
#
# # 提交表单
# element.send_keys(Keys.RETURN)

# 关闭浏览器实例以释放资源
driver.quit()