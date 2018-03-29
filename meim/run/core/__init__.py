#!/usr/bin/env python3
import os
from flask import Flask
# from flask_login import login_required, current_user, login_manager, user_loader
# import flask_login
from flask_bootstrap import Bootstrap
from core.controllers.cleanlist import melisty
from core.controllers.all_listed import all_listedmez

from core.controllers.general import controller as general
from core.controllers.login import controller as login

omnibus=Flask(__name__)

# login_manager=flask_login.LoginManager()
# login_manager.init_app(omnibus)

Bootstrap(omnibus)

omnibus.register_blueprint(general)
omnibus.register_blueprint(login)
# from core.controllers.bicycle import controller as bicycle

# omnibus.register_blueprint(bicycle)

## first part of modularization
def keymaker(omnibus, filename='secret_key'):
        pathname= os.path.join(omnibus.instance_path, filename)
        print ("pathy: ", pathname, omnibus,  omnibus.instance_path)
        try:
                omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()

        except IOError:
                parent_directory= os.path.dirname(pathname)
                if not os.path.isdir(parent_directory):
                        os.system('mkdir -p {0}'.format(parent_directory))
                os.system('head -c 24 /dev/urandom > {0}'.format(pathname))
                omnibus.config['SECRET_KEY'] = open(pathname, 'rb').read()


# from core.controllers.hihimez import hihimez
# omnibus.register_blueprint(hihimez)

def blueimportreg(filelist):
    for filename in filelist:
        strex="from core.controllers.{zz}mez import {zz}mez".format(zz=filename)
        strey="omnibus.register_blueprint({zz}mez)".format(zz=filename)
        exec(strex)
        exec(strey)

# blueimportreg(['hihi','meao', 'return'])
blueimportreg(melisty)
omnibus.register_blueprint(all_listedmez)

keymaker(omnibus)

#####
# class User(flask_login.UserMixin):
#     def __init__(self):
#         flask_login.UserMixin.__init__(self)
#
#
#
# login_manager.login_view= "login"
#
# @login_manager.user_loader
# def load_user(user_id):
#     bluepoo = flask_global.current_app.blueprints[request.blueprint]
#
#     if hasattr(blueprint, load_user):
#         return blueprint.load_user(user_id)
#
#
#
#     return User.get(user_id)
    # core.controller.checkidno
