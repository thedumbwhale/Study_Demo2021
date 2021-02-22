from db_Demo2_sql.configDB import MyPymysqlPool

phone = '15035444223';

service = MyPymysqlPool("service")

try:
    print("________service_____________")
    sqlservice = "update future_user set cms_user='1',ugc_user = '1',admin_roles='ROLE_ADMIN' where phone = " + phone;
    userInfo = service.update(sqlservice)
    print("更新成功")

except Exception as e:
    print('出现异常:', e)

service.commitTest()
service.rollbackTest()
service.closeTest()
