#!/usr/bin/env python3
from flask import Blueprint, render_template
meme_ssmez = Blueprint('meme_ssmez', __name__, url_prefix='/meme-ss')
@meme_ssmez.route('/', methods=['GET'])
def show_meme_ss():
	return render_template('meme_ssmez.html')