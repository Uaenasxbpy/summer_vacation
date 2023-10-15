# 用程序模拟浏览器向服务器请求数据
# urlib库的使用
import urllib.request
import urllib.parse

def demo(url):
    """
    使用urllib库获取网页
    :param url:
    :return:
    """
    response = urllib.request.urlopen(url)
    # HTTPresponse
    print(type(f"类型{response}"))
    content = response.read(100).decode('UTF-8')
    # print(content)
    content1 = response.readline()
    content2 = response.readlines()
    content3 = response.getcode()
    content4 = response.geturl()
    print(content4)
    content5 = response.getheaders()
    return None

def demo1(url):
    """
    下载网页中的内容 -- urllib.request.urlretrieve(url=url,filename='')
    视频.mp4，网页.html，图片.jpg。
    :param url:
    :return:
    """
    urllib.request.urlretrieve(url,'baidu.html')
    return None

def demo2(url):
    """
    UA反爬 -- user agent
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 116.0.0.0 Safari / 537.36 Edg / 116.0.1938.62'
    }
    # 请求对象的定制 -- 需要关键词传参
    request = urllib.request.Request(url=url,headers=headers)
    print(request)
    # 模拟浏览器发送请求获取网页源码
    response = urllib.request.urlopen(request)
    content = response.read().decode('UTF-8')
    print(content)
    return None

def demo3(url):
    """
    编解码
    :param url:
    :return:
    """
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
    }
    # 定制请求对象
    requesst = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(requesst)
    content = response.read().decode('utf-8')
    print(content)
    return None

def demo4(url):
    """
    编解码
    :param url:
    :return:
    """
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
    }
    name = urllib.parse.quote('丁真')
    # print(name)
    url = url + name
    print(url)
    # 定制请求对象
    requesst = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(requesst)
    content = response.read().decode('utf-8')
    print(content)
    return None

def demo_dz(url):
    """
    urlencode方法解码
    :param url:
    :return:
    """
    data = {
        'wd':'丁真',
        'sex':'男',
        'location':'中国四川省'
    }
    data = urllib.parse.urlencode(data)
    # print(data)
    url = url + data
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('UTF-8')
    print(content)
    return None

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    url1 = 'https://www.bilibili.com'
    # demo(url)
    # demo1(url)
    # demo2(url1)
    url3 = 'https://www.baidu.com/s?wd=%E4%B8%81%E7%9C%9F'
    url4 = 'https://www.baidu.com/s?'
    # demo3(url3)
    demo_dz(url4)