#!/usr/bin/env python3
from flask import Blueprint, render_template
classmez = Blueprint('classmez', __name__, url_prefix='/class')
@classmez.route('/', methods=['GET'])
def show_class():
	return render_template('classmez.html')