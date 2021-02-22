import urllib.request
import requests

# 提示说请求太频繁
# 关闭多余的连接
s = requests.session()
s.keep_alive = False

url = "https://blog.csdn.net"

#######伪装浏览器代码部分#######
headers = ("User-Agent",
           "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
#######伪装浏览器代码部分#######

data = opener.open(url).read().decode('utf-8', 'ignore')
print(data)
