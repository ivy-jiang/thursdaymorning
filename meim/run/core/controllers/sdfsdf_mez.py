#!/usr/bin/env python3
from flask import Blueprint, render_template
sdfsdf_mez = Blueprint('sdfsdf_mez', __name__, url_prefix='/sdfsdf-')
@sdfsdf_mez.route('/', methods=['GET'])
def show_sdfsdf_():
	return render_template('sdfsdf_mez.html')