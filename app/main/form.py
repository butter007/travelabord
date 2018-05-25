# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Required


class BudgetForm(FlaskForm):
    delegationName = StringField('代表团（组）名称')
    headmanName = StringField('团（组）长姓名')
    peoples = StringField('出国人数')
    countries = StringField('出访地区')
    days = StringField('批准出访天数')
    cashtypes = SelectField('外汇种类', validators=[Required()],
                            choices=[('0', '美元'), ('1', '欧元'), ('2', '日元'), ('3', '港币')])
    meals = StringField('伙食费')
    hotelexpenses = StringField('住宿费')
    publicfees = StringField('公杂费')
    traffic = StringField('交通费')
    submit = SubmitField('提交')

