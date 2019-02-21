# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:39:13 2019

@author: maria
"""

from flask import Flask, jsonify,request,render_template
from engine import *
app=Flask(__name__)



# this is home page, we want to display all tasks on this page using the /all api
@app.route("/")
def index():
    return render_template("index.html")

# this is /all api, it displays all the tasks from our database and is connected to aour home page through javascript code
@app.route("/all",methods=["GET"])
def get_all_results_one():
    if get_cursor_one("database3"):
        results=get_information_for_tasks("database3")
    return jsonify({"results" : results})

#this is /task/id get_task_from_database_and_display_by_title
@app.route("/task_id",methods=["GET","POST"])
def get_task():
    if get_cursor():
        results=get_task_from_database_and_display(3)

    return jsonify({"results" : results})




# this is /task api, it displays one tasks from our database (filtered by title) and is connected to our /task_entry_display page
@app.route("/task_title",methods=["GET","POST"])
def get_task_by_title(title):
    if get_cursor_one("database3"):
        results=get_task_from_database_and_display_by_title(title)

    return jsonify({"results" : results})



#/new_task will have the form for a new entry task and a block content in jinja which will be extended by /task_entry_display
@app.route("/new_task",methods=["GET"])
def new_task():
    return render_template("new_task.html")

#/task_entry_display  extends /new_task page ( so under the form we will have a jinja block
# - if the method will be post(right afer submitting the form) then we write that info in the database and return an empty block ( an empty/task_entry_display page)
# - if the method is get, then the block on /task_entry_display will use the api  /task and display that task
@app.route("/task_entry_display",methods=["POST"])
def task_entry_display():

    form_data = request.form
    title=form_data["title"]
    description=form_data["description"]
    date=form_data["date"]
    urgency=form_data["urgency"]
    status=form_data["status"]
    new_to_database=new_entry(title,description, date,urgency,status)
    return render_template("/task_entry_display.html", **locals())
    # else:
    #     return render_template("/task_entry_display",**locals())

if __name__ == "__main__":
    app.run(debug=True,port=5002)
