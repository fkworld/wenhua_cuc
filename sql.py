import sqlite3

class SQL(object):


    def __init__(self):
        db_name = 'wenhua.db'
        self.conn = sqlite3.connect(db_name, isolation_level=None) # 自动commit()
        self.cursor = self.conn.cursor()
        self.db_init()
        
    def db_init(self):
        # 数据库初始化，建立各种表格
        cmd_table_articles = '''
            CREATE TABLE IF NOT EXISTS articles
            (
                id              TEXT    PRIMARY KEY     NOT NULL,
                title           TEXT,
                author          TEXT,
                tag             TEXT,
                flag            TEXT,
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
                id              INTEGER     PRIMARY KEY     NOT NULL,
                account         TEXT,
                password        TEXT,
                power           TEXT
            );
        '''
        try:
            self.cursor.execute(cmd_table_articles)
            self.cursor.execute(cmd_table_admins)
            print('CREATE TABLE SUCESS.')
        except:
            print('CREATE TABLE FAILED.')
            return False

    def add_line(self, table_name, value_list):
        # 根据全属性值添加一行数据
        cmd_part = ['INSERT INTO']
        cmd_part.append(str(table_name))
        cmd_part.append('VALUES')
        cmd_part.append('(')
        cmd_part.append(','.join(map(str,value_list))) # map(str,list)的作用是对list中的所有对象作str()处理
        cmd_part.append(')')
        cmd_part.append(';')
        step = ' ' # 空格
        cmd_add_line = step.join(cmd_part)
        print(cmd_add_line)
        try:
            self.cursor.execute(cmd_add_line)
            print('ADD LINE SUCESS.')
        except:
            print('ADD LINE FAILED.')

    def update_line_single(self, table_name, value_list, target_list):
        # 根据目标更新一行数据中的一项，多项更新还没有想好怎么写
        cmd_part = ['UPDATE']
        cmd_part.append(str(table_name))
        cmd_part.append('SET')
        cmd_part.append('='.join(map(str,value_list)))
        cmd_part.append('WHERE')
        cmd_part.append('='.join(map(str,target_list)))
        cmd_part.append(';')
        step = ' '
        cmd_update_line = step.join(cmd_part)
        try:
            self.cursor.execute(cmd_update_line)
            print('UPDATE LINE SUCESS.')
        except:
            print('UPDATE LINE FAILED.')

    def delete_line(self, table_name, target_value):
        # 根据目标删除某一行的数据
        cmd_part = ['DELETE FROM']
        cmd_part.append(str(table_name))
        cmd_part.append('WHERE')
        cmd_part.append('='.join(map(str,target_list)))
        cmd_part.append(';')
        step = ' '
        cmd_delete_line = step.join(cmd_part)
        try:
            self.cursor.execute(cmd_delete_line)
            print('DELETE LINE SUCESS.')
        except:
            print('DELETE LINE FAILED.')
        
    def search_line_all(self, table_name):
        # 搜索全表，往后会改成搜索前N项，点击下一页后再搜索N项，以此类推
        cmd_part = ['SELECT * FROM']
        cmd_part.append(str(table_name))
        cmd_part.append(';')
        step = ' '
        cmd_search_line_all = step.join(cmd_part)
        try:
            self.cursor.execute(cmd_search_line_all)
            return self.cursor.fetchall() # 返回结果
            print('SEARCH LINE ALL SUCESS.')
        except:
            print('SEARCH LINE ALL FAILED.')
        
    def search_line_targetly(self, table_name, target_list):
        # 根据目标搜索某一行数据
        cmd_part = ['SELECT * FROM']
        cmd_part.append(str(table_name))
        cmd_part.append('WHERE')
        cmd_part.append('='.join(map(str,target_list)))
        cmd_part.append(';')
        step = ' '
        cmd_search_line_targetly = step.join(cmd_part)
        print(cmd_search_line_targetly)
        try:
            self.cursor.execute(cmd_search_line_targetly)
            return self.cursor.fetchall()
            print('SEARCH LINE TARGETLY SUCESS.')
        except:
            print('SEARCH LINE TARGETLY FAILED.')