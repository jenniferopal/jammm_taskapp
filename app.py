# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:52:39 2019

@author: 612383287
"""
from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
from engine import *
app= Flask(__name__)
@app.route("/taskapi/<int:id>",methods=["GET"])
def get_all_results():
    if get_cursor():
        print(id)
        results=get_task_from_database_and_display(id)
    
    return jsonify({"results" : results})

@app.route("/api",methods=['POST'])
def createTask():
    requestData = request.results();

    if get_cursor():
        cursor.execute("INSERT INTO tasks (title, date, description,urgency) VALUES (%s, %s, %s, %s)", (requestData["title"],requestData["date"],requestData["description"],requestData["urgency"]))
    conn.commit()

    return "OK"

@app.route("/api",methods=['PUT'])
def updateTask():
    requestData = request.results();

    if get_cursor():
        cur.execute("UPDATE tasks SET title=%s, date=%s, description=%s, urgency=%s WHERE id=%s", (requestData["title"],requestData["date"],requestData["description"],requestData["urgency"]))
        conn.commit()

    return "OK"

@app.route("/api/<int:id>",methods=['DELETE'])
def deleteTask(id):
    requestData = request.results();
    if get_cursor():
        cur.execute("DELETE FROM tasks WHERE title=%s", (title,))
        conn.commit()

    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
    
    
