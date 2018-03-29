#!/usr/bin/env python3
from flask import Blueprint, render_template
listmez = Blueprint('listmez', __name__, url_prefix='/list')
@listmez.route('/', methods=['GET'])
def show_list():
	return render_template('listmez.html')