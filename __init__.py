import os
from flask import Flask, render_template, request, redirect, session, url_for
import db
from pprint import pprint

app = Flask(__name__)    #create Flask object

@app.route("/")
def root():
    return redirect("/onepager")

@app.route("/onepager")
def page():

    data = {}
    resources = db.get_resources()
    
    # parsing the data that needs to be pushed to the html page
    for _,_,files in os.walk("data"):
        for f in files:
            if "txt" not in f:
                files.remove(f)
    
    # creating a file that can be pushed to the html template
    for f in files:
        data[f[:-4]] = db.parse_text(f)

    # for bug fixing - to see what files are showing up
    # keys = list(data.keys())
    # print (keys)


    return render_template("home_page.html", data=data, resources=resources)

@app.route("/onepager/faqs")
def faq():
    return "this is an faq page"

@app.route("/onepager/citations")
def cite():
    citations = db.get_citations()
    return render_template("citations.html",citations=citations)

 
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
