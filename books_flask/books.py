from pymysql import connect
from pymysql.cursors import DictCursor
from setting import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

class Book(object):
    def __init__(self):
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor = self.conn.cursor(DictCursor) #这个可以让他返回字典形式

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_books_infos_limit(self):
        sql = 'select * from book_infos limit 1'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            print(temp)
            data.append(temp)
        return data
