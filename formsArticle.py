from flask_wtf import Form
from wtforms import StringField,BooleanField,SubmitField,SelectField,TextAreaField
from wtforms.validators import Required,Length

class ArticleForm(Form):
    title=StringField('标题',validators=[Required(),Length(1,64)])
    author=StringField('作者',validators=None)
    tag_id=SelectField('分类',coerce=int,choices=[(1,'通知'),(2,'展示'),(3,'交流'),(4,'说明')])
    flag_id=SelectField('权限',coerce=int,choices=[(1,'正常发布文档'),(2,'修改中文档'),(3,'系统文档')])
    context_html=TextAreaField('主内容编辑区[HTML]') #HTML源码编辑器
    ps_html=TextAreaField('备注内容编辑区[HTML]') #HTML源码编辑器
    submit=SubmitField('提交')

    def set_form_data(self,article):
        self.title.data=article.title
        self.author.data=article.author
        self.tag_id.data=article.tag_id
        self.flag_id.data=article.flag_id
        self.context_html.data=article.context_html
        self.ps_html.data=article.ps_html