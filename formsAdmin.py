from flask_wtf import Form
from wtforms import SubmitField,StringField,BooleanField,ValidationError
from wtforms.validators import Required,Length,EqualTo

class LoginForm(Form):
    answer=StringField('MIRROR,MIROR,WHO IS THE MOST BEAUTIFUL?',validators=[Required(),Length(1,64)])
    remember_me=BooleanField('保持登录状态')
    submit=SubmitField('登录')

    def verify_answer(self,your_answer):
        if your_answer=='fy':#登录口令
            return True
        else:
            return False