#!/usr/bin/env python3
from flask import Blueprint, render_template
s_g_smez = Blueprint('s_g_smez', __name__, url_prefix='/s g s')
@s_g_smez.route('/', methods=['GET'])
def show_s_g_s():
	return render_template('s_g_smez.html')