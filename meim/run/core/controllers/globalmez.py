#!/usr/bin/env python3
from flask import Blueprint, render_template
globalmez = Blueprint('globalmez', __name__, url_prefix='/global')
@globalmez.route('/', methods=['GET'])
def show_global():
	return render_template('globalmez.html')