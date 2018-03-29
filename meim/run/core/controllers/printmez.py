#!/usr/bin/env python3
from flask import Blueprint, render_template
printmez = Blueprint('printmez', __name__, url_prefix='/print')
@printmez.route('/', methods=['GET'])
def show_print():
	return render_template('printmez.html')