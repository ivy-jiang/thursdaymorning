#!/usr/bin/env python3
from flask import Blueprint, render_template
else_statementmez = Blueprint('else_statementmez', __name__, url_prefix='/else statement')
@else_statementmez.route('/', methods=['GET'])
def show_else_statement():
	return render_template('else_statementmez.html')