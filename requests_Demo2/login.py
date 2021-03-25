import requests, json

with open("./jsonData/login/loginUrl.txt", "r") as f:
    loginUrl = f.read()

with open("./jsonData/login/loginInfo.json", "r") as f:
    data = f.read()

with open("./jsonData/login/loginInfo.json", "r") as f:
    header = f.read()
    headers={header}

dataJson = json.dumps(data)
print("登录信息："+dataJson)
r = requests.post(loginUrl, dataJson,headers)
print("返回值:", r.json())

print("执行成功")
