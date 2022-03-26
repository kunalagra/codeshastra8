
from helpers.mailer import *
from helpers.hashpass import *
from helpers.database import *
from app import app
from flask import request, session
import pandas as pd
import json


def checkloginusername():
    username = request.form["username"]
    check = db.find(username)
    if check is None:
        return "No User"
    else:
        return "User exists"


def checkloginpassword():
    username = request.form["username"]
    a = db.find(username)
    b = db.cell(a.row, 4).value
    password = request.form["password"]
    hashpassword = getHashed(password)
    if hashpassword == b:
        session["username"] = username
        return "correct"
    else:
        return "wrong"


def checkusername():
    username = request.form["username"]
    check = db.find(username)
    if check is None:
        return "Available"
    else:
        return "Username taken"

def getData():
    work = studb.worksheet(session['username'])
    #Skip the heading
    ab = work.get_all_values()[1:]
    return ab

def registerUser():
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]        
    values[3] = getHashed(values[3])
    values = values[:-1]
# data = dict(zip(fields, values))
# user_data = json.loads(json.dumps(data))
# user_data["password"] = getHashed(user_data["password"])
# user_data["confirmpassword"] = getHashed(user_data["confirmpassword"])
    db.append_row(values)
    studb.add_worksheet(title=values[1],rows='1',cols='10')
    studb.worksheet(values[1]).append_row(["Start","End","Position","Sleep Disturbance"])
