import sys

from db_Demo2_sql.configDB import MyPymysqlPool

userId = '578982'
phone = '15035444223'
app_client_id = '8'

mall = MyPymysqlPool("mall")
print("________mall_____________")
sqlmallA1 = "select * from ums_member where id = " + str(userId)
mallUserInfo = mall.select(sqlmallA1)
if str(mallUserInfo) == "False":
    print("查无此人！")
    sys.exit(0)
else:
    sqlmallA2 = "UPDATE ums_member SET allow_distribution = null WHERE phone =" + str(phone)
    mall.update(sqlmallA2)

sqlmallA3 = "select * from ums_member where id = " + str(userId)
mallUserInfo = mall.select(sqlmallA3)

referrerAA = str(mallUserInfo[0][21])
# print(referrerAA)
if str(mallUserInfo[0][21]) == '1':
    allow_distribution = '白名单'
else:
    allow_distribution = '非白名单'
print("添加非白名单成功！")
# print("查询结果(成员表）：" + str(mallUserInfo))
print("此人为" + allow_distribution + "账号！！！")

# 释放资源
mall.dispose()
