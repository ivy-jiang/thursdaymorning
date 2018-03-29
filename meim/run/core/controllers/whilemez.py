#!/usr/bin/env python3
from flask import Blueprint, render_template
whilemez = Blueprint('whilemez', __name__, url_prefix='/while')
@whilemez.route('/', methods=['GET'])
def show_while():
	return render_template('whilemez.html')