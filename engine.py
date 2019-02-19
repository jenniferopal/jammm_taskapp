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


def get_task_from_database_and_display(title):
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
        
#    print(results)
    return results



        
 