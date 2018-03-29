#!/usr/bin/env python3
from flask import Blueprint, render_template
if_sdfsdfmez = Blueprint('if_sdfsdfmez', __name__, url_prefix='/if-sdfsdf')
@if_sdfsdfmez.route('/', methods=['GET'])
def show_if_sdfsdf():
	return render_template('if_sdfsdfmez.html')