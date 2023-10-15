import urllib.parse
import urllib.request
def demo1(base_url):
    """
    urlencode应用场景：多个参数
    :return:
    """
    data = {
        'wd':'周杰伦',
        'sex':'男',
        'location':'中国台湾'
    }
    new_data = urllib.parse.urlencode(data)
    # print(a)
    url = base_url + new_data
    print(url)
    # 获取网页源码
    headers = {
        'User-Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 117.0.0.0Safari / 537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    return None

if __name__ == '__main__':
    # 基础网址
    base_url = "https://www.baidu.com/s?"
    demo1(base_url)
