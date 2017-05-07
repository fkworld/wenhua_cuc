from modelsArticle import Article
from modelsAdmin import Admin
from sql import SQL

if __name__=='__main__':
    sql = SQL()
    table_name = 'articles'
    column_list = ['txt_markdown']
    key_word = 'tes'
    result = sql.search_full_text(table_name, column_list, key_word)
    result2 = sql.cursor.execute('SELECT * FROM articles WHERE txt_markdown LIKE \'%tes%\' ').fetchall()
    print(result)
    print(result2)