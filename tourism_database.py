import pymysql
import time
import datetime

class tourism_database:

    # Constructor
    def __init__(self):
        # Load mysql database connection config
        host = "127.0.0.1"
        user = "root"
        password = "99189918"
        db = "bangcoktest"

        # get mysql database connection
        self.conn = pymysql.connect(host     = host,
                                    user     = user,
                                    password = password,
                                    db       = db)
        # get cursor
        self.cursor = self.conn.cursor()


    def add_tourism_list(self, tourism_list):
        for temp_tourism in tourism_list:
            sql = "insert into crawling_tourism (ContentName, ProductName) values "
            for temp_tourism_item in temp_tourism['content']:
                sql += "('%s', '%s'), " % (temp_tourism['content_name'], temp_tourism_item)
            sql = sql[:-2]

            try:
                self.cursor.execute(sql)
                self.conn.commit()
                print(sql)
            except:
                self.conn.rollback()
                print("ERROR : add tourism list")


    def delete_tourism_list(self):
        sql = "delete from crawling_tourism"

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print(sql)
        except:
            self.conn.rollback()
            print("ERROR : delete tourism list")


    def get_tourism_list(self):
        sql = "select * from crawling_tourism"
        result_list = list()

        try:
            print(sql)

            self.cursor.execute(sql)
            self.conn.commit()

            raw_list = list(self.cursor.fetchall())

            if (raw_list != []):
                for temp in raw_list:
                    result_list.append(temp)

        except:
            self.conn.rollback()
            print("ERROR : get tourism list")

        return result_list

    def close(self):
        self.cursor.close()
        self.conn.close()