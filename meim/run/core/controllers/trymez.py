#!/usr/bin/env python3
from flask import Blueprint, render_template
trymez = Blueprint('trymez', __name__, url_prefix='/try')
@trymez.route('/', methods=['GET'])
def show_try():
	return render_template('trymez.html')