# -*- coding: utf-8 -*-
import requests
import json

s = requests.session()
url = 'http://api.map.baidu.com/location/ip?ak=4frSAk8ARf8LqZaLHZRcNOyqQMzzzOEc&ip=115.239.212.133&coor=bd09ll'
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'}

response = s.get(url, headers=header, timeout=200)
print(response.text)

json = json.loads(response.text)

print('位置：' + str(json['content']['address']))
print('详述：' + str(json['content']['address_detail']))
print('商圈：' + str(json['content']['address_detail']['province']))

print('经度：' + str(json['content']['point']['x']))
print('维度：' + str(json['content']['point']['y']))
