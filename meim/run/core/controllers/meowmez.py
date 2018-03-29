#!/usr/bin/env python3
from flask import Blueprint, render_template
meowmez = Blueprint('meowmez', __name__, url_prefix='/meow')
@meowmez.route('/', methods=['GET'])
def show_meow():
	return render_template('meowmez.html')