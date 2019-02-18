from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

db_path = 'db/test.db'
conn = sqlite3.connect('db/test.db')
c = conn.cursor()

#class Todo(db_path):
#    id = db_path(db_path.Column(db_path, primary_key=True))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=["POST"])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    return '<h1>{}</h1>'.format(request.form['todoItem'])





if __name__=='__main__':
    app.run(debug=True)
