import pymysql

conn = None
cursor = None

try:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, database="python", charset='utf8')
    cursor = conn.cursor()
    cursor.execute("delete from students where name ='孙悟空'")
    conn.commit()
except Exception as err:
    print("数据库查询出错", str(err))
    # 出错回滚事务
    conn.rollback()

finally:
    cursor.close()
    conn.close()
