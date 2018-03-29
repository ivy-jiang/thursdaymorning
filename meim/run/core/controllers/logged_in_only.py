#!/usr/bin/env python3
from flask import Blueprint, render_template
logged_in_only = Blueprint('logged_in_only', __name__, url_prefix='/logged_in_only')


@logged_in_only.route('/', methods=['GET'])
def show_logged_in_only():
	return render_template('logged_in_only.html')
