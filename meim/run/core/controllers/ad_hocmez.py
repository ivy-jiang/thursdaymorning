#!/usr/bin/env python3
from flask import Blueprint, render_template
ad_hocmez = Blueprint('ad_hocmez', __name__, url_prefix='/ad hoc')
@ad_hocmez.route('/', methods=['GET'])
def show_ad_hoc():
	return render_template('ad_hocmez.html')