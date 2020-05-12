# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("index.html")

##need to edit to add personal information, links to other pages

#optional test
@app.route("/1006")
def ten_oh_six():
    return render_template("1006.html")
    #server error
    
@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")


#start the server
if __name__ == "__main__":
    app.run()
    
#NOTES
    #20:00 to link to other sections of website
    #23:00 git start
    #36:00 github repository