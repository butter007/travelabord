from flask import render_template, session, redirect, url_for, current_app, request
import json

from app.main.form import BudgetForm
from ..models import StandardFee
from . import main


@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route("/add", methods=['GET', 'POST'])
def add():
    countryFeeDict = {}
    standardfeelist = StandardFee.query.all()
    for item in standardfeelist:
        feeList = []
        feeList.append(item.country)
        feeList.append(item.type)
        feeList.append(item.hotelexpense)
        feeList.append(item.boardwages)
        feeList.append(item.extrafee)
        countryFeeDict[item.id] = feeList
    jsonstr = json.dumps(countryFeeDict)
    print (jsonstr)
    return render_template('add.html', jsonstr=jsonstr)


@main.route("/addexecute", methods=['POST'])
def addexecute():
    print(request.form['province'])
    print(request.form['approve'])
    return render_template('index.html')
