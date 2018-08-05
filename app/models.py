# -*- coding:utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class StandardFee(db.Model):
    __tablename__ = 'standardfees'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64), unique=True)
    type = db.Column(db.String(8))
    hotelexpense = db.Column(db.Float)
    boardwages = db.Column(db.Float)
    extrafee = db.Column(db.Float)

    def __init__(self, country, type, hotelexpense, boardwages, extrafee):
        self.country = country
        self.type = type
        self.hotelexpense = hotelexpense
        self.boardwages = boardwages
        self.extrafee = extrafee

    @staticmethod
    def insert_standardfee():
        standardfeejapan = StandardFee('日本', '日元', 13000, 10000, 5000)
        standardfeekorea = StandardFee('韩国', '美元', 110, 70, 35)
        standardfeesingapore = StandardFee('新加坡', '美元', 110, 55, 40)
        standardfeehongkong = StandardFee('香港', '港币', 800, 350, 100)
        standardfeemacau = StandardFee('澳门', '港币', 800, 350, 100)
        standardfeetaiwan = StandardFee('台湾', '美元', 100, 60, 40)
        standardfeevietnam = StandardFee('越南', '美元', 70, 40, 30)
        standardfeecambodia = StandardFee('柬埔寨', '美元', 70, 40, 30)
        standardfeeburma = StandardFee('缅甸', '美元', 70, 40, 30)
        standardfeebengal = StandardFee('孟加拉', '美元', 90, 50, 45)
        standardfeesafrica = StandardFee('南非', '美元', 110, 50, 35)
        standardfeegerman = StandardFee('德国', '欧元', 110, 60, 38)
        standardfeefrance = StandardFee('法国', '欧元', 110, 60, 38)
        standardfeeitaly = StandardFee('意大利', '欧元', 110, 60, 38)
        standardfeeothreuropean = StandardFee('其他欧元国家', '欧元', 100, 60, 38)
        standardfeedanmark = StandardFee('丹麦', '美元', 120, 80, 50)
        standardfeesverige = StandardFee('瑞典', '美元', 120, 80, 50)
        standardfeenoreg = StandardFee('挪威', '美元', 120, 80, 50)
        standardfeeswitzerland = StandardFee('瑞士', '美元', 120, 80, 50)
        standardfeeicelandd = StandardFee('冰岛', '美元', 120, 80, 50)
        standardfeeengland = StandardFee('英国', '英镑', 90, 45, 35)
        standardfeerussia = StandardFee('俄罗斯', '美元', 120, 45, 40)
        standardfeeusa = StandardFee('美国', '美元', 140, 55, 45)
        standardfeecanada = StandardFee('加拿大', '美元', 120, 55, 45)
        standardfeemaxcio = StandardFee('墨西哥', '美元', 90, 50, 45)
        standardfeeaustria = StandardFee('澳大利亚', '美元', 110, 60, 50)
        standardfeenewzealand = StandardFee('新西兰', '美元', 110, 60, 45)
        standardfeebrasil = StandardFee('巴西', '美元', 100, 50, 45)
        standardfeechile = StandardFee('智利', '美元', 100, 50, 45)
        standardfeeargentina = StandardFee('阿根廷', '美元', 100, 50, 45)
        db.session.add_all([standardfeejapan, standardfeekorea, standardfeesingapore,
                            standardfeehongkong, standardfeemacau, standardfeetaiwan,
                            standardfeevietnam, standardfeecambodia, standardfeeburma,
                            standardfeebengal, standardfeesafrica, standardfeegerman,
                            standardfeefrance, standardfeeitaly, standardfeeothreuropean,
                            standardfeedanmark, standardfeesverige, standardfeenoreg,
                            standardfeeswitzerland, standardfeeicelandd, standardfeeengland,
                            standardfeerussia, standardfeeusa, standardfeecanada,
                            standardfeemaxcio, standardfeeaustria, standardfeenewzealand,
                            standardfeebrasil, standardfeechile, standardfeeargentina
                            ])
        db.session.commit()


class Teaminfo(db.Model):
    __tablename__ = 'teaminfos'
    id = db.Column(db.Integer, primary_key=True)
    peoplesname = db.Column(db.String(256))
    peoples = db.Column(db.String(8), nullable=False)
    single = db.Column(db.String(8), nullable=True)
    days = db.Column(db.String(8), nullable=False)
    expectdate = db.Column(db.String(16), nullable=False)
    area1 = db.Column(db.String(64), nullable=False)
    area1days = db.Column(db.String(8), nullable=False)
    cashtype1 = db.Column(db.String(36), nullable=False)
    area2 = db.Column(db.String(64), nullable=True)
    area2days = db.Column(db.String(8), nullable=True)
    cashtype2 = db.Column(db.String(36), nullable=True)
    area3 = db.Column(db.String(64), nullable=True)
    area3days = db.Column(db.String(8), nullable=True)
    cashtype3 = db.Column(db.String(36), nullable=True)
    applicationdate = db.Column(db.String(16), nullable=True)
    deleteflag = db.Column(db.Integer, default=0)
    certiflag = db.Column(db.Integer,nullable=True)
    itemfee = db.relationship("Itemfee", backref="teaminfo", uselist=False, lazy="joined")
    actualItemfee = db.relationship("ActualItemfee", backref="teaminfo", uselist=False, lazy="joined")



class Itemfee(db.Model):
    __tablename__ = 'itemfees'
    id = db.Column(db.Integer, primary_key=True)
    fee12 = db.Column(db.String(16), nullable=True)
    fee13 = db.Column(db.String(16), nullable=True)
    fee14 = db.Column(db.String(256), nullable=True)
    fee22 = db.Column(db.String(16), nullable=True)
    fee23 = db.Column(db.String(16), nullable=True)
    fee24 = db.Column(db.String(256), nullable=True)
    fee32 = db.Column(db.String(16), nullable=True)
    fee33 = db.Column(db.String(16), nullable=True)
    fee34 = db.Column(db.String(256), nullable=True)
    fee42 = db.Column(db.String(16), nullable=True)
    fee43 = db.Column(db.String(16), nullable=True)
    fee44 = db.Column(db.String(256), nullable=True)
    fee52 = db.Column(db.String(16), nullable=True)
    fee53 = db.Column(db.String(16), nullable=True)
    fee54 = db.Column(db.String(256), nullable=True)
    fee62 = db.Column(db.String(16), nullable=True)
    fee63 = db.Column(db.String(16), nullable=True)
    fee64 = db.Column(db.String(256), nullable=True)
    fee72 = db.Column(db.String(16), nullable=True)
    fee73 = db.Column(db.String(16), nullable=True)
    fee74 = db.Column(db.String(256), nullable=True)
    fee82 = db.Column(db.String(16), nullable=True)
    fee83 = db.Column(db.String(16), nullable=True)
    fee84 = db.Column(db.String(256), nullable=True)
    fee92 = db.Column(db.String(16), nullable=True)
    fee93 = db.Column(db.String(16), nullable=True)
    fee94 = db.Column(db.String(256), nullable=True)
    fee102 = db.Column(db.String(16), nullable=True)
    fee103 = db.Column(db.String(16), nullable=True)
    fee104 = db.Column(db.String(256), nullable=True)
    Teaminfo_id = db.Column(db.Integer, db.ForeignKey('teaminfos.id'))

    class ActualItemfee(db.Model):
        __tablename__ = 'actualItemfees'
        id = db.Column(db.Integer, primary_key=True)
        actualpeoples = db.Column(db.String(8),nullable=True)
        actualdays = db.Column(db.String(8), nullable=False)
        departuredate = db.Column(db.String(16), nullable=False)
        entrydate = db.Column(db.String(16), nullable=False)
        acturalarea1 = db.Column(db.String(64), nullable=False)
        actualarea1days = db.Column(db.String(8), nullable=False)
        actualcashtype1 = db.Column(db.String(36), nullable=False)
        actualarea2 = db.Column(db.String(64), nullable=True)
        actualarea2days = db.Column(db.String(8), nullable=True)
        actualcashtype2 = db.Column(db.String(36), nullable=True)
        actualarea3 = db.Column(db.String(64), nullable=True)
        actualarea3days = db.Column(db.String(8), nullable=True)
        actualcashtype3 = db.Column(db.String(36), nullable=True)
        fee15 = db.Column(db.String(16), nullable=True)
        fee16 = db.Column(db.String(16), nullable=True)
        fee17 = db.Column(db.String(256), nullable=True)
        fee25 = db.Column(db.String(16), nullable=True)
        fee26 = db.Column(db.String(16), nullable=True)
        fee27 = db.Column(db.String(256), nullable=True)
        fee35 = db.Column(db.String(16), nullable=True)
        fee36 = db.Column(db.String(16), nullable=True)
        fee37 = db.Column(db.String(256), nullable=True)
        fee45 = db.Column(db.String(16), nullable=True)
        fee46 = db.Column(db.String(16), nullable=True)
        fee47 = db.Column(db.String(256), nullable=True)
        fee55 = db.Column(db.String(16), nullable=True)
        fee56 = db.Column(db.String(16), nullable=True)
        fee57 = db.Column(db.String(256), nullable=True)
        fee65 = db.Column(db.String(16), nullable=True)
        fee66 = db.Column(db.String(16), nullable=True)
        fee67 = db.Column(db.String(256), nullable=True)
        fee75 = db.Column(db.String(16), nullable=True)
        fee76 = db.Column(db.String(16), nullable=True)
        fee77 = db.Column(db.String(256), nullable=True)
        fee85 = db.Column(db.String(16), nullable=True)
        fee86 = db.Column(db.String(16), nullable=True)
        fee87 = db.Column(db.String(256), nullable=True)
        teaminfo_id = db.Column(db.Integer, db.ForeignKey('teaminfos.id'))