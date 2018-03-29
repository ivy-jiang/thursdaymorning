#!/usr/bin/env python3
from flask import Blueprint, render_template
assertmez = Blueprint('assertmez', __name__, url_prefix='/assert')
@assertmez.route('/', methods=['GET'])
def show_assert():
	return render_template('assertmez.html')