#!/usr/bin/env python3
import sqlite3
from flask import Blueprint, session, render_template, redirect, url_for, request, flash

controller = Blueprint('login', __name__, url_prefix='/login')

@controller.route('/', methods=['GET', 'POST'])
def show_login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        idz=request.form['idask']
        passwordz=request.form['passwordz']
        validornah= checkuser(idz,passwordz)

        if validornah == "Bad inputz" or validornah == "Bad ID & password input":
            return render_template('login.html', message2="Try login again.")

        else:
            idnum=validornah[0]
        # if idz=="ivy" and passwordz=="abc":
            flash('You were successfully logged in!')
            return (redirect(url_for('general.show_frontpage')))
            # return render_template('index.html', message2="Good login")


# @controller.route('/checkuser')
def checkuser(idname,password):
    try:
        name=str(idname)
        passw=str(password)
        connection=sqlite3.connect('setup/master.db', check_same_thread=False)
        cursor=connection.cursor()
        cursor.execute("SELECT * from users where username='{}' and password= '{}';".format(name, passw))
        getii=cursor.fetchone()
        propname=str(getii[1])
        proppass=str(getii[2])
        propid=int(getii[0])
        print (getii)
        cursor.close()
        connection.close()
        if getii == None:
            return ("Bad input.")
        else:
            return (("Successful login", propid, propname, proppass))

    except:
        return ("Bad ID & password input")
