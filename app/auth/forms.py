# -*- coding:utf-8 -*-
# author: uchen
# created: 2015-04-27
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1,64), Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登 录')


class RegistrationForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1,64), Email()])
    username = StringField(u'用户名', validators=[Required()])
    password = PasswordField(u'密码', validators=[Required(),
                            EqualTo('password2', message=u'两次密码必须一致.')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已被注册.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已被使用.')
