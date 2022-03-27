
from helpers.mailer import *
from helpers.hashpass import *
from helpers.database import *
from helpers.face_detection import faceDetection
from app import app
from flask import request, session, Response
import pandas as pd
import json
import cv2

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
def Gpie():
    work = studb.worksheet(session['username'])
    data={
    "Position":work.col_values(3),
    "Start":work.col_values(1),
    }
    df = pd.DataFrame(data)
    df=df[1:]
    df['Start'] = df['Start'].str[:-6]

    df_g=df.groupby('Start').count().reset_index()
    return(df_g.to_dict('list'))

def getData():
    work = studb.worksheet(session['username'])
    #Skip the heading
    ab = work.get_all_values()[1:]
    return ab
def video_p():
    isthisFile=request.files.get('file')
    isthisFile.save("./"+isthisFile.filename)
    faceDetection()
    return "0"
def getSymT():
    work = studb.worksheet(session['username'])
    data={
    "Position":work.col_values(3),
    "Difference":work.col_values(4),
    }
    df = pd.DataFrame(data)
    df=df[1:]
    df['Difference'] = pd.to_numeric(df['Difference'])

    df_g=df.groupby('Position').sum().reset_index()
    return df_g.to_dict('list')

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
