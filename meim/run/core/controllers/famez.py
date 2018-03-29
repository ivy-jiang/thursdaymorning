#!/usr/bin/env python3
from flask import Blueprint, render_template
famez = Blueprint('famez', __name__, url_prefix='/fa')
@famez.route('/', methods=['GET'])
def show_fa():
	return render_template('famez.html')