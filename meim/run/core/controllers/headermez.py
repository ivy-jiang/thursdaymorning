#!/usr/bin/env python3
from flask import Blueprint, render_template
headermez = Blueprint('headermez', __name__, url_prefix='/header')
@headermez.route('/', methods=['GET'])
def show_header():
	return render_template('headermez.html')