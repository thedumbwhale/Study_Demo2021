import null as null
import requests
import json

# 提示说请求太频繁
# 关闭多余的连接
s = requests.session()
s.keep_alive = False

startUrl = 'http://10.4.40.54/api/artugc/music/page'
param = {

    "name": "",
    "musician": "",
    "lastEditUserName": "",
    "myself": 0,
    "auditStatus": [
        "COMMIT",
        "FIRSTCHECKING",
        "FIRSTREJECT",
        "SECONDCHECKING",
        "SECONDREJECT",
        "THIRDCHECKING",
        "THIRDREJECT",
        "CHECKED"],
    "sortTerm": "LAST_EDIT_TIME",
    "sortOrder": "DESC",
    "styleIds": [
    ],
    "importance": null,
    "regionId": null,
    "page": 1,
    "pageSize": 20

}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh,zh-CN;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Referer": "http://10.4.40.54:3024/",
    "Host": "10.4.40.54",
    "Content-Type": "application/json",
    "Cookie": "sid=0ac3c46d7de40c86471a3a66949f14c5; connect.sid=s%3AE3PAbWmNVQI_buY95YnQH5s8CRQbkwST.r9XUiJjMuZdGYt33udpjwORxwaXOAPcQcGDh8fbDnik; page.id=598zgpqgkokldl69sl; refer.url=http%3A%2F%2F10.4.40.54%3A3024%2F; page.prev.id=; UM_distinctid=177bf0286bf531-0e6102675cdd74-31346d-1fa400-177bf0286c0c6f; CNZZDATA1279273237=902111862-1613813847-null%7C1613813847; JSESSIONID=ED433CAD3B84D6D2154734A5138F2389; bearer=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJkdWhlbmciLCJjcmVhdGVkIjoxNjEzOTYyMjk1MDU5LCJleHAiOjE2MTQ1NjcwOTUsInVzZXJpZCI6MTc2fQ.VH0uuzIY30SeUe98OUGjgCZiBbLYONR2zCu6d7TWCS2FSCl9E9AXe_bf5Gm1IUV8D4Fov4FhJV44__6hj67_gg",
    "Proxy-Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",

}
# proxies = {"https": "https://127.0.0.1:1080",
#            "http": "http://127.0.0.1:1080"}

# response = requests.post(url=startUrl, headers=headers, proxies=proxies, json=str(param))
response = requests.post(url=startUrl, headers=headers, json=str(param))
print(response.status_code)
# print(r.content)
