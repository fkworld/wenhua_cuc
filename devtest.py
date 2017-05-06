from modelsArticle import Article
from sql import SQL

if __name__=='__main__':
    sql = SQL()
    #cmd = 'select * from admins'
    #value_list = ['654321',6]
    #result = sql.cursor.execute(cmd)
    #print(result.fetchall())

    target_list = ['id', 5]
    value_list = ['password', '111111']
    sql.update_line_single('admins',value_list, target_list)