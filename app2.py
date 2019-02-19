#CREATING THE WEB PAGE
from flask import Flask, render_template, request
app = Flask("FormApp")

@app.route("/")
def index():
    quotes = ["milly huckle."]
    return render_template("index.html", title="home", **locals())

@app.route("/form")
def form():
    return render_template("form.html", title="form")

@app.route("/task_entry", methods=["POST"])
def task_entry():
    form_data = request.form
    title = form_data['title']
    date = form_data['date']
    description = form_data['desc']
    result="ALL OK"
    return render_template("task_entry.html", title="Form confirmation", **locals())


if __name__ == "__main__":
    app.run(debug=True)
