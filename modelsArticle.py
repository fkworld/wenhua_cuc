from datetime import datetime

from sql import SQL

time_format = '%Y-%m-%d %H:%M:%S'
id_fomat = '%Y%m%d%H%M%S'

class Article(object):


    def __init__(self):
        self.table_name = 'articles'
        self.sql = SQL()
        self.tags = [
            ('NOTICE','通知'),
            ('SHOW','展示'),
            ('EXP','经验'),
            ('LOG','日志')
        ]
        self.flags = [
            ('ONLINE','在线发布文档'),
            ('OFFLINE','离线发布文档'),
            ('SYSTEM','系统文档'),
            ('BACKUP','备份文档')
        ]
        self.id = None
        self.title = None
        self.author = None
        self.tag = None
        self.flag = None
        self.create_time = None
        self.update_time = None
        self.txt_markdown = None
        self.txt_html = None
        self.reading_times = None

    def get_tag_name(self):
        return self.tag
    
    def get_flag_name(self):
        return self.flag

    def get_flag_grade(self):
        return self.flag is 'NOTICE'

    def get_create_time(self):
        return self.create_time

    def get_update_time(self):
        return self.update_time

    def get_datetime(self):
        now_time = datetime.now()
        return now_time

    def set_id(self):
        if self.id is None:
            create_time_object = datetime.strptime(self.create_time, time_format)
            self.id = create_time_object.strftime(id_fomat)

    def form_to_object(self, form):
        # 从form中获取数据，保存到对象中去
        if self.create_time is None:
            self.create_time = self.get_datetime().strftime(time_format)
        self.update_time = self.get_datetime().strftime(time_format)
        print(self.create_time)
        self.set_id()
        self.reading_times = 0 # 以后再做阅读次数的功能

        self.title = form.title.data
        self.author = form.author.data
        self.tag = form.tag.data
        self.flag = form.flag.data
        self.txt_markdown = form.txt_markdown.data
        self.txt_html = form.txt_markdown.data

    def new_article(self):
        value_list = [self.id]
        value_list.append(self.title)
        value_list.append(self.author)
        value_list.append(self.tag)
        value_list.append(self.flag)
        value_list.append(self.create_time)
        value_list.append(self.update_time)
        value_list.append(self.txt_markdown)
        value_list.append(self.txt_html)
        value_list.append(self.reading_times)
        self.sql.add_line(self.table_name, value_list)

    def update_article(self):
        value_list = [self.title]
        value_list.append(self.author)
        value_list.append(self.tag)
        value_list.append(self.flag)
        value_list.append(self.update_time)
        value_list.append(self.txt_markdown)
        value_list.append(self.txt_html)
        value_list.append(self.reading_times)
        column_list = ['title', 'author', 'tag', 'flag', 'update_time', 'txt_markdown', 'txt_html', 'reading_times']
        target_vector = ['id', self.id]
        self.sql.update_line_part(self.table_name, column_list, value_list, target_vector)

    def delete_article(self):
        target_vector = ['id', self.id]
        if self.flag == 'BACKUP':
            self.sql.delete_line_targetly(self.table_name, target_vector)
            return 'CLEAR DELETE.'
        else:
            value_vector = ['flag', 'BACKUP']
            self.sql.update_line_single(self.table_name, value_vector, target_vector)
            return 'BACKUP DELECT.'

    def result_to_object(self, sql_result):
        # sql_result：一行数据是一个元组，整个数据是一个列表；[(-),...]
        # 从sql_result中获取数据，保存到对象中去
        result_tuple = sql_result[0]
        self.id = result_tuple[0]
        self.title = result_tuple[1]
        self.author = result_tuple[2]
        self.tag = result_tuple[3]
        self.flag = result_tuple[4]
        self.create_time = result_tuple[5]
        self.update_time = result_tuple[6]
        self.txt_markdown = result_tuple[7]
        self.txt_html = result_tuple[8]
        self.reading_times = result_tuple[9]

    def result_to_object_list(self, sql_result):
        # 从sql_result中获取数据，保存为对象列表
        article_list = []
        for i in range(len(sql_result)):
            article = Article()
            article.result_to_object([sql_result.pop(0)])
            article_list.append(article)
        return article_list

    def search_by_id(self, id):
        # 根据文章id搜索数据库，返回本article对象
        target_vector = ['id', id]
        result = self.sql.search_line_targetly(self.table_name, target_vector)
        self.result_to_object(result)
    
    def search_by_tag(self, tag):
        # 根据文章tag搜索数据库，返回一个object_list
        target_vector = ['tag', tag]
        sql_result = self.sql.search_line_targetly(self.table_name, target_vector)
        return self.result_to_object_list(sql_result)
    
    def search_by_key_word(self, key_word):
        # 根据关键字进行全文搜索，以后再做的功能
        pass

    def search_all(self):
        # 搜索全部文章，返回一个object_list
        sql_result = self.sql.search_line_all(self.table_name)
        return self.result_to_object_list(sql_result)


