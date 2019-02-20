# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:39:13 2019

@author: maria
"""

from flask import Flask, jsonify,request
from engine import *
app=Flask(__name__)

dummy=[{"id":"1", "title":"lunch", "date": "15/03/2019","description":"to have something healthy for lunch", "status":"not done", "urgency":"not urgent"},
         {"id":"2", "title":"breakfast","date": "15/04/2019", "description":"to have cake at breakfast", "status":"not done", "urgency":"not urgent"},
         {"id":"3", "title":"dinner","date": "01/03/2019", "description":"to have wine for dinner", "status":"not done", "urgency":"urgent"}
         ]


@app.route("/",methods=["GET"])
def test():
    return jsonify({"message" : "This is my message!!"})

#this is using the dummy information
@app.route("/results",methods=["GET"])
def get_results():
    return jsonify({"results" : dummy})

#this is using the dummy information and only displays one task, filtered by the title(or whatever you'd want) added in the url 
@app.route("/results/<string:title>",methods=["GET"])
def get_results_title(title):
    dummy_title=[dum for dum in dummy if dum["title"] == title]
    return jsonify({"dum" : dummy_title[0]})



 






#this is connecting to our database and retrieving information from it
@app.route("/mariana",methods=["GET"])
def get_all_results():
    if get_cursor("mariana"):
        results=get_information_for_businesses_with_input_business_type_mari("Computers")
    
    return jsonify({"results" : results})




############################This is database3 ##############################################S
#this is connecting to our database fro Final Project and retrieving information from it
@app.route("/all",methods=["GET"])
def get_all_results_one():
    if get_cursor_one("database3"):
        results=get_information_for_tasks("database3")
    
    return jsonify({"results" : results})


#this is connecting to our database fro Final Project and retrieving information from it and filters it by a specific date
@app.route("/date",methods=["GET"])
def get_all_results_date():
    if get_cursor_one("database3"):
        results=filter_tasks_by_date("database3","17/02/2019")
    
    return jsonify({"results" : results})

@app.route("/all/<string:date>",methods=["GET"])
def get_all_results_filtered_by_date(date):
    if get_cursor_one("database3"):
        results=filter_tasks_by_date("database3",date)
    
    return jsonify({"results" : results})



if __name__ == "__main__":
    app.run(debug=True)
