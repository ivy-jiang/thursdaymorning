#!/usr/bin/env python3
from flask import Blueprint, render_template
requestmez = Blueprint('requestmez', __name__, url_prefix='/request')
@requestmez.route('/', methods=['GET'])
def show_request():
	return render_template('requestmez.html')