import pandas as pd
from db_Demo2_sql.configDB import MyPymysqlPool

# 二选一
userId = 578985
# userId = '578985'
# phone = '15035444223'

app_client_id = '8'

mall = MyPymysqlPool("mall")
print("________mall_____________")
sqlmallA1 = "select id,username from ums_member where id = " + str(userId)
mallUserInfo = mall.select(sqlmallA1)

df = pd.DataFrame(list(mallUserInfo), columns=["id", "username"])

# 筛选列表中，当id列中为'XXX'，所有username的值，然后转为list
userName = df.username[df['id'] == userId].tolist()
# print(userName, type(userName))
# list转string
print("username为："+''.join(userName))



# if str(mallUserInfo) == "False":
#     print("查无此人！")
#     sys.exit(0)
# else:
#     sqlmallA2 = "UPDATE ums_member SET allow_distribution = '1' WHERE phone =" + str(phone)
#     mall.update(sqlmallA2)
#
# sqlmallA3 = "select * from ums_member where id = " + str(userId)
# mallUserInfo = mall.select(sqlmallA3)
#
# referrerAA = str(mallUserInfo[0][21])
# # print(referrerAA)
# if str(mallUserInfo[0][21]) == '1':
#     allow_distribution = '白名单'
# else:
#     allow_distribution = '非白名单'
# print("添加白名单成功！")
# # print("查询结果(成员表）：" + str(mallUserInfo))
# print("此人为" + allow_distribution + "账号！！！")

# 释放资源
mall.dispose()
