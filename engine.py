# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:53:51 2019

@author: maria
"""

import sqlite3 
import requests
import sys
import json

def get_cursor(environment):
    conn=sqlite3.connect("{}_phoneBookProject2.db".format(environment))
    cursor=conn.cursor()
    print (cursor)
    return cursor, conn


def get_information_for_businesses_with_input_business_type_mari(business_type):
    cursor,connection=get_cursor("mariana")
   
    cursor.execute("SELECT business_name, telephone_number, postcode,adress_line_1,adress_line_2,adress_line_3 FROM businesses WHERE business_category=?", (business_type,))
    rows = cursor.fetchall()
    print(rows)  
    results=[]
    result={}
    for row in rows:
        result={"business_name":row[0],"phone":row[1],"postcode":row[2],"street":row[3],"city":row[4],"country":row[5]}
        print(result)
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
            
    
            
#get_information_for_tasks("database3")
#filter_tasks_by_date("database3","17/02/2019")

#get_information_for_businesses_with_input_business_type_mari("Toys")    

