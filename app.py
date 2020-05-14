# -*- coding: utf-8 -*-
###############################################################
# Name: Zoë Webb-Mack
# UNI: zwm2104
# ENGI-1006 Final
#
# File creates html website on local server using Flask.
# Functions contained here create different site pages,
# referencing template html files in folder.
###############################################################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    """Function runs html for home page, which includes personal information
    and links to other pages"""
    #return "Hello World!"
    return render_template("index.html")
##need to edit to add personal information, links to other pages
    #fix image, need to rotate and resize
    #still need doctstrings

#define routes
@app.route("/1006")
def ten_oh_six():
    """Function runs html for test 1006 page"""
    return render_template("1006.html")
    
@app.route("/classes")
def classes():
    """Function runs html for classes page, which includes information
    about my classes this semester and my favorite class"""
    return render_template("classes.html")

@app.route("/assignments")
def assignments():
    """Function runs html for assignments page, which includes information about
    our assignements in ENGI1006 and my favorite assignment"""
    return render_template("assignments.html")


#start the server
if __name__ == "__main__":
    app.run()
    
#NOTES
    #20:00 to link to other sections of website