#!/usr/bin/env python3
from flask import Blueprint, render_template
importmez = Blueprint('importmez', __name__, url_prefix='/import')
@importmez.route('/', methods=['GET'])
def show_import():
	return render_template('importmez.html')