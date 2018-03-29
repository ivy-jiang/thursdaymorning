#!/usr/bin/env python3
from flask import Blueprint, render_template
passmez = Blueprint('passmez', __name__, url_prefix='/pass')
@passmez.route('/', methods=['GET'])
def show_pass():
	return render_template('passmez.html')