from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 打开chrome浏览器
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.baidu.com/"
driver.get(url)

title = driver.title
print(title)
now_url = driver.current_url
print(now_url)
page_source = driver.page_source
# print(page_source)
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(page_source)

# 元素定位 -- 或者使用By类的语法
button = driver.find_element(By.ID, 'su')
text = driver.find_element(By.NAME, 'wd')
button1 = driver.find_element(By.XPATH, '//input[@id="su"]')
# find_elements返回的是列表
button2 = driver.find_elements(By.XPATH, '//input[@id="su"]')
# 选择器 -- 和BS4的语法一样
button3 = driver.find_element(By.CSS_SELECTOR, '#su')
# 获取连接文本
link = driver.find_element(By.LINK_TEXT, '新闻')

print(button)
print(button1)
print(button2)
print(text)
print(f"新闻链接{link}")

# 元素信息交互
input_button = driver.find_element(By.ID,'su')
input_class = input_button.get_attribute('class')
# 获取标签的属性
print(f"input的class名：{input_class}")
print(f"input的tag name：{input_button.tag_name}")
# 获取元素文本
print(f"link的text：{link.text}")

# 防止网页关闭
num = input("是否结束：Y/N")
driver.close()
