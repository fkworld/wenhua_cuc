from modelsArticle import Article
from modelsAdmin import Admin
from modelsSPEA import SPEA,NoticeBoard,WebsiteInfo
from sql import SQL


class A(object):
    def __init__(self):
        self.sql = SQL()
        self.id = 1
    def get_sql(self):
        return self.sql
    def get_id(self):
        return self.id

class B(A):
    def test(self):
        print(super().get_sql())

class C(B):
    def tt(self):
        print(super().get_sql())
        print(self.get_id())

if __name__=='__main__':
    c = C()
    c.tt()
    #gg = WebsiteInfo()
    #print(gg)