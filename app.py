# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:52:39 2019

@author: 612383287
"""
from flask import Flask, jsonify,request
from engine import *
app= Flask(__name__)
@app.route("/taskapi/<int:id>",methods=["GET"])
def get_all_results(id):
    if get_cursor():
#        print(id)
        results=get_task_from_database_and_display(id)
    
    return jsonify({"results" : results})





if __name__ == "__main__":
    app.run(debug=True, port=8080)