# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:53:51 2019

@author: maria
"""

import sqlite3
import requests
import sys
import json





def get_cursor_one(environment):
    conn=sqlite3.connect("{}.db".format(environment))
    cursor=conn.cursor()
#    print (cursor)
    return cursor, conn

def get_information_for_tasks(environment):
    cursor,connection=get_cursor_one(environment)

    cursor.execute("SELECT title, date, description,urgency,status FROM tasks")
    rows = cursor.fetchall()
#    print(rows)
    results=[]
    result={}
    for row in rows:
        result={"title":row[0],"date":row[1],"description":row[2],"status":row[3]}
#        print(result)
        results.append(result)

#    print(results)
    return results
def filter_tasks_by_date(environment,date):
    results=get_information_for_tasks(environment)
    tasks=[]
    for item in results:
        if item["date"]==date:
#            print(date)
#            print (item)
            tasks.append(item)
#    print(tasks)
    return tasks



def get_cursor():
    conn=sqlite3.connect("database3.db")
    cursor=conn.cursor()
#    print (cursor)
    return cursor, conn


def get_task_from_database_and_display(id):
    cursor,connection=get_cursor()

    cursor.execute("SELECT title, date, description,urgency,status FROM tasks WHERE id=?", (id,))
    rows = cursor.fetchall()
#    print(rows)
    results=[]
    result={}
    for row in rows:
        result={"title":row[0],"date":row[1],"description":row[2],"urgency":row[3],"status":row[4]}
#        print(result)
        results.append(result)

    print(results)
    return results

def get_task_from_database_and_display_by_title(title):
     cursor,connection=get_cursor()

     cursor.execute("SELECT title, date, description,urgency,status FROM tasks WHERE title=?", (title,))
     rows = cursor.fetchall()
    #    print(rows)
     results=[]
     result={}
     for row in rows:
         result={"title":row[0],"date":row[1],"description":row[2],"urgency":row[3],"status":row[4]}
    #        print(result)
         results.append(result)

     print(results)
     return results

def new_entry(title,description, date,urgency,status):
    cursor,connection=get_cursor()
    cursor.execute("INSERT INTO tasks(title,description, date,urgency,status) VALUES(?,?,?,?,?)", (title,description, date,urgency,status))
    connection.commit()
    return description

def delete_entry(title):
    cursor,connection=get_cursor()
    cursor.execute("DELETE FROM tasks WHERE title=?", (title,))
    connection.commit()
    return "OK"
delete_entry("Run")
#get_task_from_database_and_display(3)
