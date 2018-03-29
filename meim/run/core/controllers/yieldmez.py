#!/usr/bin/env python3
from flask import Blueprint, render_template
yieldmez = Blueprint('yieldmez', __name__, url_prefix='/yield')
@yieldmez.route('/', methods=['GET'])
def show_yield():
	return render_template('yieldmez.html')