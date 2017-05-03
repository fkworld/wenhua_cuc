from modelsArticle import Article
from sql import SQL

if __name__=='__main__':
    sql = SQL()
    test = ('fy')
    cmd = 'select * from admins where account =?'
    print(cmd)
    result  = sql.cursor.execute(cmd, test)
    print(result.fetchall())