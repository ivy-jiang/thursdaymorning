#!/usr/bin/env python3
from flask import Blueprint, render_template
REQUESTSmez = Blueprint('REQUESTSmez', __name__, url_prefix='/REQUESTS')
@REQUESTSmez.route('/', methods=['GET'])
def show_REQUESTS():
	return render_template('REQUESTSmez.html')