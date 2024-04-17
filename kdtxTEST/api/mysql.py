import pymysql


class mysqlAPI:
    conn = None

    @classmethod
    def __get_conn(cls):

        if cls.conn is None:
            cls.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, database="python",
                                       charset='utf8')
        return cls.conn

    @classmethod
    def __close_conn(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None

    @classmethod
    def select_one(cls, sql):
        cursor = None
        res = None
        try:
            # 建立连接
            cls.conn = cls.__get_conn()
            # 获取游标
            cursor = cls.conn.cursor()
            # 查询
            cursor.execute(sql)
            # 提取一条结果
            res = cursor.fetchone()
        except Exception as err:
            print("查询数据出错", str(err))
        finally:
            cursor.close()
            # 关闭连接
            cls.__close_conn()
            # 返回结果
            return res

    @classmethod
    def uid_db(cls, sql):
        cursor = None
        try:
            # 建立连接
            cls.conn = cls.__get_conn()
            # 获取游标
            cursor = cls.conn.cursor()
            # 对表进行操作
            cursor.execute(sql)
            print()
            # 提交更改
            cls.conn.commit()
        except Exception as erorr:
            print('数据更改出错', str(erorr))
            # 事务回滚
            cls.conn.rollback()
        finally:
            cursor.close()
            cls.__close_conn()


if __name__ == '__main__':
    mysqlAPI.uid_db("insert into students(studentNo,name,sex,age,class) values ('014','李逵', '男','35','2班')")
    mysqlAPI.uid_db("update students set hometown = '湖南' where name = '李逵'")
    info = mysqlAPI.select_one("select * from students where studentNo = '014'")
    print(info)
