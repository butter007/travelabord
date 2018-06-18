from flask import render_template, session, redirect, url_for, current_app, request

from app.main.form import BudgetForm
from ..models import StandardFee
from . import main


@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route("/add", methods=['GET', 'POST'])
def add():
    countryDict = {}
    standardfeelist = StandardFee.query.all()
    for item in standardfeelist:
        countryDict[item.id] = item.country
    print(countryDict)
    return render_template('add.html', data=countryDict.items())


@main.route("/addexecute", methods=['POST'])
def addexecute():
    print(request.form['province'])
    print(request.form['approve'])
    return render_template('index.html')
