#!/usr/bin/env python3
from flask import Blueprint, render_template
ismez = Blueprint('ismez', __name__, url_prefix='/is')
@ismez.route('/', methods=['GET'])
def show_is():
	return render_template('ismez.html')