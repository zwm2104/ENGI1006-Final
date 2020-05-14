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
import web_scrape as ws

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    """Function runs html for home page, which includes personal information
    and links to other pages"""
    
    #return homepage template
    return render_template("index.html")

#define routes
@app.route("/1006")
def ten_oh_six():
    """Function runs html for test 1006 page"""
    
    #return 1006 page template
    return render_template("1006.html")
    
@app.route("/classes")
def classes():
    """Function runs html for classes page, which includes information
    about my classes this semester and my favorite class"""
    
    #return classes page template
    return render_template("classes.html")

@app.route("/assignments")
def assignments():
    """Function runs html for assignments page, which includes information about
    our assignements in ENGI1006 and my favorite assignment"""
    
    #return assignments page template
    return render_template("assignments.html")

@app.route("/links")
def links_page():
    """Function prints list of urls scraped from website using web_scrape function"""
    
    #return list of urls
    return "<!DOCTYPE html><html><head><!--specifies title of the page !--><title>Links</title><head><body>{}</body></html>".format(ws.link_scrape("https://366weirdmovies.com"))

#start the server
if __name__ == "__main__":
    app.run()
    