#CREATING THE WEB PAGE
from flask import Flask, render_template, request, jsonify
from engine import *
app = Flask("FormApp")

@app.route("/")
def index():
    return render_template("index.html", title="home", **locals())

#THE FORM
@app.route("/form")
def form():
    return render_template("form.html", title="form")

@app.route("/form_output", methods=["POST"])
def form_output():
    form_data = request.form
    title = form_data['title']
    date = form_data['date']
    description = form_data['description']
    result="ALL OK"
    return render_template("form_output.html", title="Form confirmation", **locals())


#GET ONE RESULT
@app.route("/taskapi/<int:id>",methods=["GET"])
def get_one_result(id):
    if get_cursor():
#        print(id)
        results=get_task_from_database_and_display(id)

    return jsonify({"results" : results})

#GET ALL RESULTS
@app.route("/all",methods=["GET"])
def get_all_results():
    if get_cursor_one("database3"):
        results=get_information_for_tasks("database3")

    return jsonify({"results" : results})



if __name__ == "__main__":
    app.run(debug=True, port=8000)
