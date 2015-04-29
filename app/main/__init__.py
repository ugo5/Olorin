# -*- coding:utf-8 -*-
# author: uchen
# created: 2015-04-26
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
