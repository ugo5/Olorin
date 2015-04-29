# -*- coding:utf-8 -*-
# author: uchen
# created: 2015-04-26
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['POST', 'GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
	    # ...
    	return redirect(url_for('.index'))
    return render_template('index.html', 
	                        form=form, name=session.get('name'), 
							known=session.get('known', False), 
	                        current_time=datetime.now())
