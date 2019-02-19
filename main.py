#PROJECT TASK MANAGER- CREATING THE DATABASE

import sqlite3
#import time
#import datetime

conn = sqlite3.connect('database3.db')
c = conn.cursor()


def create_database():
    c.execute('CREATE TABLE IF NOT EXISTS tasks(id integer primary key, title TEXT, date TEXT, description TEXT, urgency TEXT, status TEXT)')
    
    
def data_entry():
    c.execute("INSERT INTO tasks VALUES(NULL ,'Run' , '03/10/1999', 'exercising is fun','important','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Clean my room' , '19/02/2019', 'cleaning is fun','unimportant','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Gardening' , '18/02/2019', 'Gardening is fun','important','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Bake a cake' , '17/02/2019', 'Baking is fun','important','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Go shopping' , '17/02/2019', 'Shopping is fun','unimportant','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Book an eye test' , '16/02/2019', 'Eye tests are fun','important','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Complete coding course' , '15/02/2019', 'Coding is fun','important','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Write a novel' , '14/02/2019', 'Writing is fun','unimportant','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Listen to music' , '14/02/2019', 'Music is fun','important','incomplete')")
    c.execute("INSERT INTO tasks VALUES(NULL ,'Have a hair cut' , '13/02/2019', 'Hair cuts are fun','important','incomplete')")
    
    
    conn.commit()





create_database()
data_entry()
c.close()
conn.close()

