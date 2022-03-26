# Flask Setup
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import os
from flask import Flask, jsonify, request, abort, render_template
app = Flask(__name__)

# Google Sheets API Setup
credential = ServiceAccountCredentials.from_json_keyfile_name("{}\\helpers\\cred.json".format(os.getcwd()),["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets",
"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"])

client = gspread.authorize(credential)
o = client.open("Users")
db = o.worksheet('UIDs')
studb = client.open("Data")
