#!/usr/bin/env python3
from flask import Blueprint, render_template
flask_loginmez = Blueprint('flask_loginmez', __name__, url_prefix='/flask_login')
@flask_loginmez.route('/', methods=['GET'])
def show_flask_login():
	return render_template('flask_loginmez.html')