#!/usr/bin/env python3
from flask import Blueprint, render_template
returnmez = Blueprint('returnmez', __name__, url_prefix='/return')
@returnmez.route('/', methods=['GET'])
def show_return():
	return render_template('returnmez.html')