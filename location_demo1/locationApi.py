# coding:utf-8
import sys
import json
import urllib.request


def get_ip_information(ip):
    url = 'http://api.map.baidu.com/location/ip?ak=4frSAk8ARf8LqZaLHZRcNOyqQMzzzOEc&ip=' + ip + '&coor=bd09ll'
    req1 = urllib.Request(url)
    req = urllib.request(url)
    page = urllib.urlopen(req, timeout=10)
    data_json = page.read()
    data_dic = json.loads(data_json)
    if (data_dic.has_key("content")):
        content = data_dic["content"]
        address = content["address"]
        address_detail = content["address_detail"]
        print("该IP地址的具体位置为：")
        print(address["address_detail"]['province'])
        print(address_detail)

        if (content.has_key("pois")):
            print("该IP地址附近POI信息如下：")
            pois = content["pois"]
            for index in range(len(pois)):
                pois_name = pois[index]["name"]
                pois_address = pois[index]["address"]
                print(pois_name, pois_address)
    else:
        print('IP地址定位失败！！！')


# print('位置：' + str(json['content']['address']))
# print('详述：' + str(json['content']['address_detail']))
# print('商圈：' + str(json['content']['address_detail']['province']))
#
# print('经度：' + str(json['content']['point']['x']))
# print('维度：' + str(json['content']['point']['y']))


if __name__ == '__main__':
    get_ip_information('115.239.212.133')
