#!/usr/bin/env python3
from flask import Blueprint, render_template
continuemez = Blueprint('continuemez', __name__, url_prefix='/continue')
@continuemez.route('/', methods=['GET'])
def show_continue():
	return render_template('continuemez.html')