#!/usr/bin/env python3
from flask import Blueprint, render_template
Flaskmez = Blueprint('Flaskmez', __name__, url_prefix='/Flask')
@Flaskmez.route('/', methods=['GET'])
def show_Flask():
	return render_template('Flaskmez.html')