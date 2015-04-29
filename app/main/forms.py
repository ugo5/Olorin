# -*- coding:utf-8 -*-
# author: uchen
# created: 2015-04-27
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError


class NameForm(Form):
    name = StringField('What is your name?', Validators=[Required()])
    submit = SubmitField('Submit')
