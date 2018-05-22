# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required


class BudgetForm(FlaskForm):
    delegationName = StringField('代表团（组）名称')
    headmanName = StringField('团（组）长姓名')

    submit = SubmitField('提交')
