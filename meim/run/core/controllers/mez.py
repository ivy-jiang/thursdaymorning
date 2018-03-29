#!/usr/bin/env python3
from flask import Blueprint, render_template
mez = Blueprint('mez', __name__, url_prefix='/')
@mez.route('/', methods=['GET'])
def show_():
	return render_template('mez.html')