from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, Email

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(),Length(1,64)])
    password = PasswordField('密码',validators=[Required()])
    password_repeat = PasswordField('重复密码',validators=[Required()])
    email = StringField('邮件',validators=[Required(),Length(1,64),Email('请输入正确的邮箱')])
    introduce = StringField('介绍', validators=[Required(),Length(1,64)])
    submit = SubmitField('注册')

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[Required(),Length(1,64)])
    password = PasswordField('密码',validators=[Required()])
    submit = SubmitField('登录')

class PostForm(FlaskForm):
    title = StringField('标题')
    content = StringField('正文')
    submit = SubmitField('发布')