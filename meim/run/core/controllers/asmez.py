#!/usr/bin/env python3
from flask import Blueprint, render_template
asmez = Blueprint('asmez', __name__, url_prefix='/as')
@asmez.route('/', methods=['GET'])
def show_as():
	return render_template('asmez.html')