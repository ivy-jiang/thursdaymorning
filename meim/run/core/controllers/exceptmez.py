#!/usr/bin/env python3
from flask import Blueprint, render_template
exceptmez = Blueprint('exceptmez', __name__, url_prefix='/except')
@exceptmez.route('/', methods=['GET'])
def show_except():
	return render_template('exceptmez.html')