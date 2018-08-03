from flask import render_template, session, redirect, url_for, current_app, request
import json
from ..models import Teaminfo, Itemfee, StandardFee
from .. import db
from ..models import StandardFee
from . import main
import time


@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route("/add", methods=['GET', 'POST'])
def add():
    id = request.args.get("id",'')

    teaminfo = Teaminfo.query.get(id)
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
    if id:
        return render_template('add01.html', teaminfo=teaminfo, jsonstr=jsonstr, data=countryFeeDict.items())
    else:
        return render_template('add01.html',  jsonstr=jsonstr, data=countryFeeDict.items())


@main.route("/addexecute", methods=['GET', 'POST'])
def addexecute():
    teaminfo = Teaminfo(peoplesname=request.form.get('peoplesname', ''),
                        peoples=request.form.get('peoples', 0),
                        single=request.form.get('single', 0),
                        days=request.form.get('days', 0),
                        expectdate=request.form.get('expectdate', ''),
                        area1=request.form.get('area1', ''),
                        area1days=request.form.get('area1days', 0),
                        cashtype1=request.form.get('cashtype1', ''),
                        area2=request.form.get('area2', ''),
                        area2days=request.form.get('area2days', 0),
                        cashtype2=request.form.get('cashtype2', ''),
                        area3=request.form.get('area3', ''),
                        area3days=request.form.get('area3days', 0),
                        cashtype3=request.form.get('cashtype3', ''),
                        applicationdate=time.strftime('%Y-%m-%d', time.localtime()))
    itemfee = Itemfee(fee12=request.form.get('fee12', 0),
                      fee13=request.form.get('fee13', 0),
                      fee14=request.form.get('fee14', ''),
                      fee22=request.form.get('fee22', 0),
                      fee23=request.form.get('fee23', 0),
                      fee24=request.form.get('fee24', ''),
                      fee32=request.form.get('fee32', 0),
                      fee33=request.form.get('fee33', 0),
                      fee34=request.form.get('fee34', ''),
                      fee42=request.form.get('fee42', 0),
                      fee43=request.form.get('fee43', 0),
                      fee44=request.form.get('fee44', ''),
                      fee52=request.form.get('fee52', 0),
                      fee53=request.form.get('fee53', 0),
                      fee54=request.form.get('fee54', ''),
                      fee62=request.form.get('fee62', 0),
                      fee63=request.form.get('fee63', 0),
                      fee64=request.form.get('fee64', ''),
                      fee72=request.form.get('fee72', 0),
                      fee73=request.form.get('fee73', 0),
                      fee74=request.form.get('fee74', ''),
                      fee82=request.form.get('fee82', 0),
                      fee83=request.form.get('fee83', 0),
                      fee84=request.form.get('fee84', ''),
                      fee92=request.form.get('fee92', 0),
                      fee93=request.form.get('fee93', 0),
                      fee94=request.form.get('fee94', ''),
                      fee102=request.form.get('fee102', 0),
                      fee103=request.form.get('fee103', 0),
                      fee104=request.form.get('fee104', ''),
                      teaminfo=teaminfo)
    db.session.add(teaminfo)
    db.session.add(itemfee)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route("/jsonlist", methods=['GET', 'POST'])
def jsonlist():
    # offset=0&limit=5
    jsonlist = []
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    totals = Teaminfo.query.count()
    # teaminfolist 查询数据包含一个itemfee对象
    teaminfolist = Teaminfo.query.filter(Teaminfo.deleteflag == 0).limit(limit).offset(offset)
    standardFeelist = StandardFee.query.all()
    stdcountry = {}
    for item in standardFeelist:
        stdcountry[str(item.id)] = item.country
    for item in teaminfolist:
        itemdict = item.__dict__
        itemdict['area1'] = stdcountry.get(itemdict['area1'], '')
        itemdict.pop('_sa_instance_state', None)
        itemfee = itemdict.get('itemfee')
        itemdict.pop('itemfee', None)
        itemdict.update(itemfee.__dict__)
        itemdict.pop('_sa_instance_state', None)
        jsonlist.append(itemdict)
    return json.dumps({'rows': jsonlist, "total": totals})


@main.route("/delete", methods=['GET', 'POST'])
def delete():
    id = request.args.get('id')
    teaminfo = Teaminfo.query.get(id)
    teaminfo.deleteflag = 1
    db.session.add(teaminfo)
    return json.dumps("success")
