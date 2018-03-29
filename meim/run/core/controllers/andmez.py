#!/usr/bin/env python3
from flask import Blueprint, render_template
andmez = Blueprint('andmez', __name__, url_prefix='/and')
@andmez.route('/', methods=['GET'])
def show_and():
	return render_template('andmez.html')