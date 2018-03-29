#!/usr/bin/env python3

from flask import Blueprint, render_template, flash

controller = Blueprint('general', __name__, url_prefix='')

@controller.route('/', methods=['GET'])
def show_frontpage():
        return render_template('index.html')
