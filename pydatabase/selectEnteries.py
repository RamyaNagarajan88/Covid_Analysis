import psycopg2

connection=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="mydb2020")
cur=connection.cursor()
# sqlQuery='''select usstates.code, populationcensus.state, populationcensus.pop 
# from usstates inner join populationcensus 
# on usstates.state=populationcensus.state'''

# cur.execute(sqlQuery)
# states=cur.fetchall()
# statesPop=dict(tuple(states))

sqlQuery='''select usstates.code, usstates.state 
from usstates'''
cur.execute(sqlQuery)
states=cur.fetchall()
print(dict(tuple(states)))

