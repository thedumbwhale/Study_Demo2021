import sys

from db_Demo2_sql.configDB import MyPymysqlPool

userId = '578982'
phone = '15035444223'
app_client_id = '8'

service = MyPymysqlPool("service")
print("________service_____________")
sqlserviceA1 = "select * from future_user where phone = " + phone
userInfo = service.select(sqlserviceA1)
if str(userInfo) == "False":
    print("查无此人！")
    sys.exit(0)
else:
    userId = userInfo[0][0]
    wei_xin_union_id = userInfo[0][15]

sqlserviceA2 = "delete  from future_user where phone = " + phone
service.delete(sqlserviceA2)
# service.commitTest()
sqlserviceA3 = "select * from future_user where phone = " + phone
userInfoA3 = service.select(sqlserviceA3)
if str(userInfoA3) == "False":
    print("future_user (用户表）删除成功-phone。")
else:
    print("删除失败！")
    print("查询结果（用户表）：" + str(userInfo))
    sys.exit(0)

sqlserviceB1 = "delete  from future_user where wei_xin_union_id = '%s'" % (wei_xin_union_id)
service.delete(sqlserviceB1)
sqlserviceB2 = "select * from future_user where wei_xin_union_id = '%s'" % (wei_xin_union_id)
userInfoB2 = service.select(sqlserviceB2)
if str(userInfoB2) == "False":
    print("future_user (用户表）删除成功-wei_xin_union_id。")
else:
    print("删除失败！")
    print("查询结果(以微信绑定用户表）：" + str(userInfoB2))
    sys.exit(0)

sqlserviceC2 = "delete  from user_account_access_info where user_id = " + str(
    userId) + " and app_client_id = " + str(app_client_id)
service.delete(sqlserviceC2)

sqlserviceC3 = "select * from user_account_access_info where user_id = " + str(
    userId) + " and app_client_id = " + str(app_client_id)
user_acess = service.select(sqlserviceC3)
if str(user_acess) == "False":
    print("user_account_access_info (上级表）删除成功。")
else:
    print("删除失败！")
    print("查询结果(上级表）：" + str(user_acess))
    sys.exit(0)

# 释放资源
service.dispose()

print("**********************************")

mall = MyPymysqlPool("mall")
print("________mall_____________")
sqlmallA1 = "select * from ums_member where id = " + str(userId)
mallUserInfo = mall.select(sqlmallA1)
if str(mallUserInfo) == "False":
    print("查无此人！")
    sys.exit(0)
else:
    sqlmallA2 = "delete  from ums_member where id = " + str(userId)
    mall.delete(sqlmallA2)

sqlmallA3 = "select * from ums_member where id = " + str(userId)
mallUserInfo = mall.select(sqlmallA3)
if str(mallUserInfo) == "False":
    print("ums_member(成员表）删除成功：")
else:
    print("删除失败！")
    print("查询结果（用户表）：" + str(mallUserInfo))
    sys.exit(0)

sqlmallB1 = "delete  from ums_member_client_info where user_id =  " + str(userId) + " and app_client_id = " + str(
    app_client_id)
mall.delete(sqlmallB1)
sqlmallB2 = "select * from ums_member_client_info where user_id =  " + str(userId) + " and app_client_id = " + str(
    app_client_id)
mallReferrer = mall.select(sqlmallB2)
if str(mallReferrer) == "False":
    print("user_account_access_info (上级表）删除成功。（我的上级信息清空完毕）")
else:
    print("删除失败！")
    referrerA = str(mallReferrer[0][2])
    if str(mallReferrer[0][2]) == '0':
        referrerA = '无'
    print("我的id userid：" + str(mallReferrer[0][1]) + ", 我的上线 referrer：" + referrerA)
    sys.exit(0)

print("__________________________")
sqlmallC1 = "delete from ums_member_client_info where referrer = " + str(userId) + " and app_client_id = " + str(
    app_client_id)
mall.delete(sqlmallC1)
sqlmallC2 = "select * from ums_member_client_info where referrer = " + str(userId) + " and app_client_id = " + str(
    app_client_id)
mallReferrerMe = mall.select(sqlmallC2)
if str(mallReferrerMe) == "False":
    print("user_account_access_info (上级表）删除成功。(我的下级清空完毕)")
else:
    print("删除失败！")
    print("查询结果(我的上线表）：" + str(mallReferrerMe))
    print("我的id userid：" + str(mallReferrerMe[0][1]), "我的上线 referrer：" + str(mallReferrerMe[0][2]))
    sys.exit(0)

# 释放资源
mall.dispose()
