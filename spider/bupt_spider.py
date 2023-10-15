from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import requests
import re

def remove_non_chinese_characters(text:str) -> str:
    """
    清除标题中的特殊字符
    :param text:
    :return:
    """
    str_chinese = re.sub('[^\u4e00-\u9fa5]+', '', text)
    return str_chinese

def down_load_picture():
    """
    下载图片并保存
    :return:
    """
    for i in range(12):
        picture = driver.find_element(By.XPATH, '//*[@id="line_u11_'+str(i)+'"]/a/div/img')
        title = driver.find_element(By.XPATH, '//*[@id="line_u11_'+str(i)+'"]/a')
        src = picture.get_attribute('src')
        picture_title = title.get_attribute('title')
        picture_title_clean = remove_non_chinese_characters(picture_title)
        # print(picture_title_clean)

        # 下载图片
        response = requests.get(src)
        image_path = f'images/{picture_title_clean+".jpg"}'
        with open(image_path, 'wb') as f:
            f.write(response.content)

if __name__ == '__main__':

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
    # print("Title:", title)
    now_url = driver.current_url
    # print(now_url)

    # 获取文本框对象
    input_button = driver.find_element(By.ID, 'kw')
    # 在文本框里面输入关键字
    input_button.send_keys('北京邮电大学')
    time.sleep(2)
    # 点击百度一下
    input_button_bd = driver.find_element(By.ID, 'su')
    input_button_bd.click()
    time.sleep(2)

    # 点击进入官方网站
    button1 = driver.find_element(By.XPATH, '//*[@id="4"]/div/div[1]/h3/a[1]')
    button1.click()
    time.sleep(2)

    #获取当前页的所有句柄
    num = driver.window_handles
    driver.switch_to.window(num[1])

    # 进入新闻网页
    button2 = driver.find_element(By.XPATH, '//*[@id="timeline-part"]/div/div[1]/div[1]/div/p/a[1]')
    button2.click()
    time.sleep(2)

    # 进入光影北邮
    button3 = driver.find_element(By.XPATH, '//*[@id="vivo-head"]/div[2]/div/div[2]/ul/li[10]/a')
    button3.click()
    time.sleep(2)
    down_load_picture()

    # 下一页
    button4 = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div/div[1]/span[1]/span[6]/a')
    button4.click()
    time.sleep(2)
    down_load_picture()
    # 退出
    driver.quit()