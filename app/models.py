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
                            standardfeemaxcio,standardfeeaustria, standardfeenewzealand,
                            standardfeebrasil,standardfeechile, standardfeeargentina
                            ])
        db.session.commit()
