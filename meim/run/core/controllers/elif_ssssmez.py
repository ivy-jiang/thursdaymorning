#!/usr/bin/env python3
from flask import Blueprint, render_template
elif_ssssmez = Blueprint('elif_ssssmez', __name__, url_prefix='/elif ssss')
@elif_ssssmez.route('/', methods=['GET'])
def show_elif_ssss():
	return render_template('elif_ssssmez.html')