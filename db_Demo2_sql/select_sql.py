import sys

from db_Demo2_sql.configDB import MyPymysqlPool

# UserId = '578973';
phone = '15035444223'
app_client_id = '6'

service = MyPymysqlPool("service")

print("________service_____________")
sqlservice = "select * from future_user where phone = " + phone
userInfo = service.select(sqlservice)
if str(userInfo) == "False":
    print("查无此人！")
    sys.exit(0)
else:
    userId = userInfo[0][0]
    wei_xin_union_id = userInfo[0][15]
    print("查询结果（用户表）：" + str(userInfo))
    print("查询userid：" + str(userId))
    print("查询wei_xin_union_id：" + str(wei_xin_union_id))

sqlservice2 = "select * from user_account_access_info where user_id = " + str(
    userId) + " and app_client_id = " + str(app_client_id)
user_acess = service.select(sqlservice2)
if str(user_acess) == "False":
    print("查无此人！")
else:
    print("查询结果(上级表）：" + str(user_acess))

sqlservice3 = "select * from future_user where wei_xin_union_id = '%s'" % (wei_xin_union_id)
user_weixin = service.select(sqlservice3)
if str(user_weixin) == "False":
    print("查无此人！")
else:
    print("查询结果(以微信绑定用户表）：" + str(user_weixin))

# 释放资源
service.dispose()

mall = MyPymysqlPool("mall")
print("________mall_____________")
sqlmall = "select * from ums_member where id = " + str(userId)
mallUserInfo = mall.select(sqlmall)
if str(mallUserInfo) == "False":
    print("查无此人！")
else:
    print("查询结果(成员表）：" + str(mallUserInfo))

sqlmall2 = "select * from ums_member_client_info where user_id =  " + str(userId) + " and app_client_id = " + str(
    app_client_id)
mallReferrer = mall.select(sqlmall2)
if str(mallReferrer) == "False":
    print("查无此人！")
else:
    referrerA = str(mallReferrer[0][2])
    if str(mallReferrer[0][2]) == '0':
        referrerA = '无'
    print("我的id userid：" + str(mallReferrer[0][1]) + ", 我的上线 referrer：" + referrerA)

print("__________________________")
sqlmall3 = "select * from ums_member_client_info where referrer = " + str(userId)
mallReferrerMe = mall.select(sqlmall3)
if str(mallReferrerMe) == "False":
    print("查无此人！")
else:
    print("查询结果(我的上线表）：" + str(mallReferrerMe))
    print("我的id userid：" + str(mallReferrerMe[0][1]), "我的上线 referrer：" + str(mallReferrerMe[0][2]))

# 释放资源
mall.dispose()
