from flask import Flask, render_template, request, jsonify
import sqlite3
from engine import *

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Form page to add a new task
@app.route('/add_task', methods=["GET"])
def add_task():
        return render_template('task.html')

# API page for all tasks (IN USE ON HOME PAGE)
@app.route("/all",methods=["GET"])
def get_all_results_one():
    if get_cursor():
        results=get_information_for_tasks("database3")

    return jsonify({"results" : results})


# API page for one task (NOT IN USE)
@app.route("/task",methods=["GET"])
def get_all_results_one_id():
    if get_cursor_one("database3"):
        results=get_task_from_database_and_display(3)

    return jsonify({"results" : results})

# This page extends task page and displays the last task entry
@app.route("/add_task_display",methods=["POST"])
def task_entry_display():

    form_data = request.form
    title=form_data["title"]
    description=form_data["description"]
    date=form_data["date"]
    urgency=form_data["urgency"]
    status=form_data["status"]
    new_to_database=new_entry(title,description, date,urgency,status)
    return render_template("/add_task_display.html", **locals())

# this is deleting a task
@app.route("/task_delete/<string:title>",methods=["GET"])
def task_delete(title):


    delete_database=delete_entry(title)
    return render_template("/index.html", **locals())


if __name__=='__main__':
    app.run(debug=True)
