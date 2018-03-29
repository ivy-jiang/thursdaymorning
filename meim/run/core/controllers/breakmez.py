#!/usr/bin/env python3
from flask import Blueprint, render_template
breakmez = Blueprint('breakmez', __name__, url_prefix='/break')
@breakmez.route('/', methods=['GET'])
def show_break():
	return render_template('breakmez.html')