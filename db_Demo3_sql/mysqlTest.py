from configparser import ConfigParser
import pymysql

cp = ConfigParser()
cp.read('../mysql.conf')

host = cp.get("mysql", "db_host")
port = cp.getint("mysql", "db_port")
user = cp.get("mysql", "db_user")
password = cp.get("mysql", "db_password")
database = cp.get("mysql", "db_database")

# 打开数据库连接
db = pymysql.connect(host=host,
                     port=port,
                     user=user,
                     password=password,
                     db=database
                     )

# 使用cursor()方法创建一个游标对象: cursor
cursor = db.cursor()

# 使用execute()方法执行SQL语句并输出结果
cursor.execute("select * from future_user where phone = 18858644223")

for row in cursor.fetchall():
    print(row)

# 关闭游标对象
cursor.close()

# 关闭数据库连接
db.close()
