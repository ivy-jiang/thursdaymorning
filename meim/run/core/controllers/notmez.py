#!/usr/bin/env python3
from flask import Blueprint, render_template
notmez = Blueprint('notmez', __name__, url_prefix='/not')
@notmez.route('/', methods=['GET'])
def show_not():
	return render_template('notmez.html')