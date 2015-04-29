# -*- coding:utf-8 -*-
# author: uchen
# created: 2015-04-27
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
