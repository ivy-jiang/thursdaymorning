#!/usr/bin/env python3
from flask import Blueprint, render_template
frommez = Blueprint('frommez', __name__, url_prefix='/from')
@frommez.route('/', methods=['GET'])
def show_from():
	return render_template('frommez.html')