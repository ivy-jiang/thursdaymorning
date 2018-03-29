#!/usr/bin/env python3
from flask import Blueprint, render_template
defmez = Blueprint('defmez', __name__, url_prefix='/def')
@defmez.route('/', methods=['GET'])
def show_def():
	return render_template('defmez.html')