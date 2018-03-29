#!/usr/bin/env python3
from flask import Blueprint, render_template
del_fdsdfdsfmez = Blueprint('del_fdsdfdsfmez', __name__, url_prefix='/del fdsdfdsf')
@del_fdsdfdsfmez.route('/', methods=['GET'])
def show_del_fdsdfdsf():
	return render_template('del_fdsdfdsfmez.html')