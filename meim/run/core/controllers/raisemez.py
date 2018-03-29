#!/usr/bin/env python3
from flask import Blueprint, render_template
raisemez = Blueprint('raisemez', __name__, url_prefix='/raise')
@raisemez.route('/', methods=['GET'])
def show_raise():
	return render_template('raisemez.html')