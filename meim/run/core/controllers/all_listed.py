#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect, url_for
all_listedmez = Blueprint('all_listedmez', __name__, url_prefix='/all_listed')
@all_listedmez.route('/', methods=['GET'])
def show_all_listed():
	return render_template('all_listed.html')