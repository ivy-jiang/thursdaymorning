#!/usr/bin/env python3
from flask import Blueprint, render_template
execmez = Blueprint('execmez', __name__, url_prefix='/exec')
@execmez.route('/', methods=['GET'])
def show_exec():
	return render_template('execmez.html')