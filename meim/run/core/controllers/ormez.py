#!/usr/bin/env python3
from flask import Blueprint, render_template
ormez = Blueprint('ormez', __name__, url_prefix='/or')
@ormez.route('/', methods=['GET'])
def show_or():
	return render_template('ormez.html')