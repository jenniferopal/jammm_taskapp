from flask import Flask, jsonify,request,render_template
from engine import *
app=Flask(__name__)
#this is connecting to our database fro Final Project and retrieving information from it
@app.route("/all",methods=["GET"])
def get_all_results_one():
    if get_cursor_one("database3"):
        results=get_information_for_tasks("database3")

    return jsonify({"results" : results})

if __name__ == "__main__":
    app.run(debug=True)
