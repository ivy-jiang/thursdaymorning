#!/usr/bin/env python3
from flask import Blueprint, render_template
not_headermez = Blueprint('not_headermez', __name__, url_prefix='/not_header')
@not_headermez.route('/', methods=['GET'])
def show_not_header():
	return render_template('not_headermez.html')