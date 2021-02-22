import pymysql


def select_db(sql, database):
    db = pymysql.connect(host='10.3.246.80',
                         port=3306,
                         user='readwrite',
                         passwd='Marble@d6',
                         db=database)
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    db.close()
    return data


if __name__ == "__main__":
    # UserId = '578973';
    phone = '15035444223';
    app_client_id = '6';

    print("________service_____________")
    sqlservice = "select * from future_user where phone = " + phone;
    userInfo = select_db(sqlservice, 'futureservice');
    userId = userInfo[0][0]
    wei_xin_union_id = userInfo[0][15]

    print("查询结果（用户表）：%s" % str(userInfo))
    print("查询userid：%s" % str(userId))
    print("查询wei_xin_union_id：%s" % str(wei_xin_union_id))

    sqlservice2 = "select * from user_account_access_info where user_id = " + str(
        userId) + " and app_client_id = " + str(app_client_id);
    user_acess = select_db(sqlservice2, 'futureservice');
    print("查询结果(上级表）：%s" % str(user_acess))

    sqlservice3 = "select * from future_user where wei_xin_union_id = 'oimQ55pdRJLontB7szIe36qX4V6s';"
    user_weixin = select_db(sqlservice3, 'futureservice');
    print("查询结果(以微信绑定用户表）：%s" % str(user_weixin))

    print("________mall_____________")
    sqlmall = "select * from ums_member where id = " + str(userId);
    mallUserInfo = select_db(sqlmall, 'future_mall');
    print("查询结果(成员表）：%s" % str(mallUserInfo))

    sqlmall2 = "select * from ums_member_client_info where user_id =  " + str(userId) + " and app_client_id = 6;"
    mallReferrer = select_db(sqlmall2, 'future_mall');
    print("查询结果(成员上线表）：%s" % str(mallReferrer))
    print("我的id userid：%s" % str(mallReferrer[0][1]), "我的上线 referrer：%s" % str(mallReferrer[0][2]))

    print("__________________________")
    sqlmall3 = "select * from ums_member_client_info where referrer = " + str(userId);
    mallReferrerMe = select_db(sqlmall3, 'future_mall');
    print("查询结果(我的上线表）：%s" % str(mallReferrerMe))
    print("我的id userid：%s" % str(mallReferrerMe[0][1]), "我的上线 referrer：%s" % str(mallReferrerMe[0][2]))
