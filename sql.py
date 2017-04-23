import sqlite3

class SQL(object):


    def __init__(self):
        db_name = 'wenhua.db'
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    def db_init(self):
        # 数据库初始化，建立各种表格
        cmd_table_articles = '''
            CREATE TABLE IF NOT EXISTS articles
            (
                id              TEXT    PRIMARY KEY     NOT NULL,
                title           TEXT,
                author          TEXT,
                tag             INTEGER,
                flag            INTEGER,
                create_time     TEXT,
                update_time     TEXT,
                txt_markdown    TEXT,
                txt_html        TEXT,
                reading_times   INTEGER
            );
        '''
        cmd_table_admins = '''
            CREATE TABLE IF NOT EXISTS admins
            (
                id              TEXT    PRIMARY KEY     NOT NULL,
                account         TEXT,
                password        TEXT,
                power           INTEGER
            );
        '''
        try:
            self.cursor.execute(cmd_table_articles)
            self.cursor.execute(cmd_table_admins)
            print('CREATE TABLE SUCESS.')
        except:
            print('CREATE TABLE FAILED.')
            return False