#!/usr/bin/env python3
from flask import Blueprint, render_template
inmez = Blueprint('inmez', __name__, url_prefix='/in')
@inmez.route('/', methods=['GET'])
def show_in():
	return render_template('inmez.html')