#!/usr/bin/env python3
from flask import Blueprint, render_template
finallymez = Blueprint('finallymez', __name__, url_prefix='/finally')
@finallymez.route('/', methods=['GET'])
def show_finally():
	return render_template('finallymez.html')