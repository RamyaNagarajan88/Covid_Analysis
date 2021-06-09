import psycopg2
import pandas as pd


connection=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="mydb2020")
cur=connection.cursor()

with open('E:/Ramya/brushUps/Basics//CASE_STUDIES/COVID/Data_Collection/Data/covidhistorydata.csv','r') as rf:
    next(rf) #to skip header
    cur.copy_from(rf,"covidhistorydata",sep=',')
connection.commit()

# cur.execute("select * from populationcensus where state='Texas'")
# line=cur.fetchone()
# print (line)