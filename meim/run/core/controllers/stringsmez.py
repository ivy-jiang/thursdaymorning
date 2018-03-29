#!/usr/bin/env python3
from flask import Blueprint, render_template
stringsmez = Blueprint('stringsmez', __name__, url_prefix='/strings')
@stringsmez.route('/', methods=['GET'])
def show_strings():
	return render_template('stringsmez.html')