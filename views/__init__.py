from cgitb import reset
import re
from urllib import response
from flask import render_template, request, redirect, url_for, session, Response
from app import app
from model import *


@app.route('/', methods=["GET"])
def home():
    if "username" in session:
        return render_template('index.html')
    else:
        return render_template('login.html')
# Register new user

@app.route('/getSessionname', methods=["GET"])
def sname():
    a =session["username"]
    return a
@app.route('/getTSum', methods=["GET"])
def timesum():
    return getSymT()

@app.route('/getpie', methods=["GET"])
def getP():
    return Gpie()

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        registerUser()
        return redirect(url_for("login"))


@app.route('/checkusername', methods=["POST"])
def check():
    return checkusername()


@app.route('/login', methods=["GET"])
def login():
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("home"))


@app.route('/checkloginusername', methods=["POST"])
def checkUserlogin():
    return checkloginusername()

@app.route('/getUsername',methods=["GET","POST","DEL","UPD"])
def getname():
    a= session['username']
    return a

@app.route('/charts', methods=["GET"])
def charts():
    return render_template("charts.html")

@app.route('/tables', methods=["GET"])
def tables():
    ab = getData()
    return render_template("tables.html", values=ab)

@app.route('/checkloginpassword', methods=["POST"])
def checkUserpassword():
    return checkloginpassword()


@app.route('/logout', methods=["GET"])  # URL for logout
def logout():  # logout function
    session.pop('username', None)  # remove user session
    return redirect(url_for("home"))  # redirect to home page with message

@app.route('/upload', methods=["POST"])
def upload():
    return video_p()

# @app.route('/getFeed',methods=["GET"])
# def getFeed():
#     return Response(Camera().gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/forgot-password', methods=["GET"])
def forgotpassword():
    return render_template('forgot-password.html')


@app.route('/404', methods=["GET"])
def errorpage():
    return render_template("404.html")


@app.route('/blank', methods=["GET"])
def blank():
    return render_template('blank.html')

