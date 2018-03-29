#!/usr/bin/env python3
from flask import Blueprint, render_template
withmez = Blueprint('withmez', __name__, url_prefix='/with')
@withmez.route('/', methods=['GET'])
def show_with():
	return render_template('withmez.html')