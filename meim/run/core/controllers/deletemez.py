#!/usr/bin/env python3
from flask import Blueprint, render_template
deletemez = Blueprint('deletemez', __name__, url_prefix='/delete')
@deletemez.route('/', methods=['GET'])
def show_delete():
	return render_template('deletemez.html')