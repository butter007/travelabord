from flask import render_template, session, redirect, url_for, current_app

from app.main.form import BudgetForm
from .. import db
from . import main


@main.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route("/add", methods=['GET', 'POST'])
def add():
    form = BudgetForm()
    return render_template('add.html', form=form)