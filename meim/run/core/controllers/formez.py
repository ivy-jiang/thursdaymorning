#!/usr/bin/env python3
from flask import Blueprint, render_template
formez = Blueprint('formez', __name__, url_prefix='/for')
@formez.route('/', methods=['GET'])
def show_for():
	return render_template('formez.html')