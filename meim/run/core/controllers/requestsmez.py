#!/usr/bin/env python3
from flask import Blueprint, render_template
requestsmez = Blueprint('requestsmez', __name__, url_prefix='/requests')
@requestsmez.route('/', methods=['GET'])
def show_requests():
	return render_template('requestsmez.html')