#!/usr/bin/env python3
from flask import Blueprint, render_template
__init__mez = Blueprint('__init__mez', __name__, url_prefix='/__init__')
@__init__mez.route('/', methods=['GET'])
def show___init__():
	return render_template('__init__mez.html')