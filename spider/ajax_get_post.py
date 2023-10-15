import urllib.request
import urllib.parse

def cerate_get_request(page):
    """
    get请求对象的定制
    :param page:
    :return:
    """
    base_url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&"
    data = {
        'start':(page - 1) * 20,
        'limit':20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    # print(url)
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 117.0.0.0Safari / 537.36'
    }
    request = urllib.request.Request(url=url,headers=headers)
    return request

def create_post_request(page):
    """
    post对象的定制
    :param page:
    :return:
    """
    base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 117.0.0.0Safari / 537.36'
    }
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    return request

def get_content(request):
    """
    获取数据
    :param request:
    :return:
    """
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def get_content_by_handler(request):
    """
    使用代理
    :param request:
    :return:
    """
    proxies = {
        'http':'118.24.219.151.16817'
    }
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content,page):
    """
    下载具体内容
    :param content:
    :param page:
    :return:
    """
    with open('get请求'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)
def down_load_post(content,page):
    """
    下载具体内容
    :param content:
    :param page:
    :return:
    """
    with open('post请求'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page = int(input("请输入起始页码:"))
    end_page = int(input("请输入结束的页码:"))
    for page in range(start_page,end_page + 1):
        # print(page)
        request = cerate_get_request(page)
        content = get_content_by_handler(request)
        down_load(content,page)

        request_post = create_post_request(page)
        content_post = get_content(request_post)
        # print(content_post)
        down_load_post(content_post,page)



