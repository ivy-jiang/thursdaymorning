#!/usr/bin/env python3
from flask import Blueprint, render_template
lambdamez = Blueprint('lambdamez', __name__, url_prefix='/lambda')
@lambdamez.route('/', methods=['GET'])
def show_lambda():
	return render_template('lambdamez.html')