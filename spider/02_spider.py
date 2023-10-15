import urllib.request
import urllib.parse
import json
def content_demo(url,data,headers):
    """

    :param url:
    :param data:
    :param headers:
    :return:
    """
    # post请求中的data数据必须是字节流，需要编码后调用encode方法
    data = urllib.parse.urlencode(data).encode('UTF-8')
    request = urllib.request.Request(url=url,data=data,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    obj = json.loads(content)
    print(obj)
    return None

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 'hello',
        'simple_means_flag': '3',
        'sign': '54706.276099',
        'token': 'e1575a9f069e29cf03ac54b34c4b5aca',
        'domain': 'common',
        'ts': '1693386311679'
    }

    headers = {
        'Cookie': 'REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1;'
                  ' BDUSS=RJVHIxdlkyRGFzc3lrZlN2cWdpSmUzRUpaV2twbWNkdktCYUhrTlFsZ1Q0bUZrRVFBQUFBJCQAAAAAAQAAAAEAAAAKCkEfAAAAAAA'
                  'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNVOmQTVTpkM3; BDUSS_BFESS=RJVHI'
                  'xdlkyRGFzc3lrZlN2cWdpSmUzRUpaV2twbWNkdktCYUhrTlFsZ1Q0bUZrRVFBQUFBJCQAAAAAAQAAAAEAAAAKCkEfAAAAAAAAAAAAAAAAAAAAAA'
                  'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABNVOmQTVTpkM3; BIDUPSID=D41CB2A3956E738A7F101A6FF'
                  'D7810E1; PSTM=1682474271; APPGUIDE_10_6_2=1; BAIDUID=93DD22074A7B9FACAF9D5F282CBBF554:SL=0:NR=10:FG=1; BAIDUID_BF'
                  'ESS=93DD22074A7B9FACAF9D5F282CBBF554:SL=0:NR=10:FG=1; BA_HECTOR=8k0g042ha124ag00010h2l0j1ietf8d1p; ZFY=KFV9JyNxvT'
                  'ldWiMsEhrch28j6tiJ:Ae0it4bf:A:AKeed4:C; ab_sr=1.0.1_ZjNhNWYwM2E5ZjAzOGFjZWQzMDM3ZDc3OWVlYzgwZmJhOWJkMGIzM2ExNWJkMmN'
                  'mZTBkMTJjMDA2NDYyYjU5NTc5MDkzOWE1MTBkYWNmZTVkODY4NDU4MWM1ODlhODE4OTdjNmI2NmZjMWQ1OGE1NWU5ZTY5YzE2ZjI3YzRiN2Q4ZmI3Yzg'
                  '1YzAwMmNlMzNlMzk1YTJhZWNkMGI3NWVmMDJmZjdmOGM1MGJjY2FjMjc0MmY0ZWRhNjQ5ZTFlY2Nm',
    }

    content_demo(url,data,headers)
