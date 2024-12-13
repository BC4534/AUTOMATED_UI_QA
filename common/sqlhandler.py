import sqlite3
import pymysql
import psycopg2
import pyodbc

class SqlHandler:
    """
    MySQL
        type: 数据库类型，对于 MySQL 总是 'mysql'。
        host: MySQL服务器的地址，例如 'localhost'。
        user: 用于连接数据库的用户名。
        password: 对应用户名的密码。
        db_name: 要连接的数据库名称。
    """
    def __init__(self, db_config):
        """初始化数据库连接"""
        self.db_config = db_config
        self.conn = self._connect_to_database()
        self.cursor = self.conn.cursor()

    def _connect_to_database(self):
        """根据配置连接到不同的数据库"""
        if self.db_config['type'] == 'sqlite':
            return sqlite3.connect(self.db_config['db_name'])
        elif self.db_config['type'] == 'mysql':
            return pymysql.connect(
                host=self.db_config['host'],
                user=self.db_config['user'],
                password=self.db_config['password'],
                database=self.db_config['db_name']
            )
        elif self.db_config['type'] == 'postgresql':
            return psycopg2.connect(
                host=self.db_config['host'],
                dbname=self.db_config['db_name'],
                user=self.db_config['user'],
                password=self.db_config['password']
            )
        elif self.db_config['type'] == 'sqlserver':
            driver = '{ODBC Driver 17 for SQL Server}'
            server = self.db_config['host']  # e.g. 'localhost'
            database = self.db_config['db_name']  # e.g. 'mydb'
            uid = self.db_config['user']  # e.g. 'myusername'
            pwd = self.db_config['password']  # e.g. 'mypassword'
            conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'
            return pyodbc.connect(conn_str)
        else:
            raise ValueError("Unsupported database type")

    def execute(self, query, params=None):
        """执行SQL语句"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def fetch_one(self, query, params=None):
        """获取查询结果的第一条记录"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            raise e

    def fetch_all(self, query, params=None):
        """获取查询结果的所有记录"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            raise e

    def close(self):
        """关闭数据库连接"""
        self.cursor.close()
        self.conn.close()

# 使用示例
if __name__ == "__main__":
    # SQL Server
    db_config_sqlserver = {
        'type': 'mysql',
        'host': 'localhost',
        'user': 'root',
        'password': '123456',
        'db_name': 'baichen'
    }
    db_mysql = MySqlServer(db_config_sqlserver)
    dblist = db_mysql.fetch_all('SELECT * FROM employees')
    for db in dblist:
        print(db)
    db_mysql.close()