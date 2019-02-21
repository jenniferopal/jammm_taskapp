# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:54:56 2019

@author: 612383287
"""

import sqlite3 
import requests
import sys
import json

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

get_task_from_database_and_display(4)

        
 