from main import db
from datetime import datetime

class Article(db.Model):
    __tablename__='articles'
    id=db.Column(db.String(14),primary_key=True)
    title=db.Column(db.String(64))
    author=db.Column(db.String(64))
    tag_id=db.Column(db.Integer)
    flag_id=db.Column(db.Integer)
    update_datetime=db.Column(db.DateTime)
    context_html=db.Column(db.Text)
    ps_html=db.Column(db.Text)

    tags=('通知','展示','交流','说明')
    flags=('系统文件','展示文件','修改中文件','删除后备份文件')

    def get_tag_name(self):
        return self.tags[self.tag_id]

    def get_flag_boolean(self):
        if self.flag_id==0 or self.flag_id==1:
            return False
        else:
            return True

    def set_flag_id(self,flag_boolean):
        if self.flag_id is not None and self.flag_id==0: #系统文件
            pass
        elif flag_boolean==False:
            self.flag_id=1 #展示文件
        else:
            self.flag_id=2 #修改中文件
        
    def set_id(self):
        if self.id is None:
            self.id=self.update_datetime.strftime('%Y%m%d%H%M%S')

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
        self.update_datetime=datetime.now()
        self.set_id()