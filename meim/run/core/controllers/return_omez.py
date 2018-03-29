#!/usr/bin/env python3
from flask import Blueprint, render_template
return_omez = Blueprint('return_omez', __name__, url_prefix='/return-o')
@return_omez.route('/', methods=['GET'])
def show_return_o():
	return render_template('return_omez.html')