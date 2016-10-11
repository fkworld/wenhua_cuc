from main import db
from datetime import datetime

class Article(db.Model):
    __tablename__='articles'
    id=db.Column(db.String(14),primary_key=True)
    title=db.Column(db.String(64))
    author=db.Column(db.String(64))
    tag_id=db.Column(db.Integer)
    flag_id=db.Column(db.Integer)
    create_datetime=db.Column(db.DateTime)
    context_html=db.Column(db.Text)
    ps_html=db.Column(db.Text)

    tags=('','通知','展示','交流','说明')
    flags=('','正常发布文档','修改中文档','系统文档','删除后服务器备份文档')

    def get_tag_name(self):
        return self.tags[self.tag_id]
    
    def get_flag_name(self):
        return self.flags[self.flag_id]

    def get_flag_grade(self):
        if self.flag_id==1:
            return True
        else:
            return False
        
    def set_id(self):
        if self.id is None:
            self.id=self.create_datetime.strftime('%Y%m%d%H%M%S')

    def delete(self):
        if self.flag_id!=4:
            self.flag_id=4
            self.update_db()
            return '文章已经从列表中删除，但是还在数据库中有备份'
        else:
            db.session.delete(self)
            db.session.commit()
            return '文章备份已经从数据库中完全删除，不可恢复'

    def update_db(self):
        db.session.add(self)
        db.session.commit()

    def set_all_by_form_6_values(self,form):
        self.title=form.title.data
        self.author=form.author.data
        self.tag_id=form.tag_id.data
        self.flag_id=form.flag_id.data
        self.context_html=form.context_html.data
        self.ps_html=form.ps_html.data
        self.create_datetime=datetime.now()
        self.set_id()