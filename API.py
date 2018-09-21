import os
import sys
import time
import json
import requests
import subprocess
from threading import Thread as thread
from flask import Flask, request, render_template, jsonify, redirect

app = Flask(__name__)


# basic get request route to see if the site is live
@app.route('/')
def status():
    return "live!"


# start addUser receives a json string with profile info name, msstateID, dormName
# start returns name of user added to Database
@app.route('/addUser', methods=['POST'])
def start(name, msstateID, dormName):

    # try to get the profile info from json.  Included so that debuggin with standard function call outside
    # of API can be used
    try:
        profile = request.json  # text from body
        name = profile["name"]
        msstateID = profile["msstateID"]
        dormName = profile["dormName"]
    except:
        pass

    # TODO: insert logic to connect to mySQL and add profile

    return str(msstateID)


# start addAdmin receives a json string with profile info name, adminID, startDate
# start returns name of user added to Database
# startDate will be of the form mmddyyyy all digits
@app.route('/addAdmin', methods=['POST'])
def start(name, adminID, startDate):

    # try to get the profile info from json.  Included so that debuggin with standard function call outside
    # of API can be used
    try:
        profile = request.json  # text from body
        name = profile["name"]
        adminID = profile["adminID"]
        startDate = profile["startDate"]
    except:
        pass

    # TODO: insert logic to connect to mySQL and add profile

    return str(adminID)

if __name__ == '__main__':
    # name, numOfProcesses, rate, stopCondition
    #print(start("profile1", 1, 30, 10))
    print(stop("profile1"))
    # app.run(host='0.0.0.0',port=9090)
    # app.run(port=9090, debug=True)
