from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,SelectField,TextAreaField
from wtforms.validators import Required,Length,EqualTo
from modelsArticle import Article

class ArticleForm(FlaskForm):
    article = Article()
    title = StringField('标题', validators=[Required(),Length(1,64)])
    author = StringField('作者', validators=None)
    tag = SelectField('分类', choices=article.tags)
    flag = SelectField('权限', choices=article.flags)
    txt_markdown = TextAreaField('markdown') # markdown编辑器
    submit = SubmitField('提交')

    def object_to_data(self,article):
        self.title.data = article.title
        self.author.data = article.author
        self.tag = article.tag
        self.flag = article.flag
        self.txt_markdown = article.txt_markdown

class LoginForm(FlaskForm):
    account = StringField('帐号', validators=[Required(), Length(1,64)])
    password = PasswordField('密码', validators=[Required(), Length(1,64)])
    remember_me = BooleanField('保持登录状态')
    submit = SubmitField('登录')
