import csv

with open('E:/Ramya/brush ups/Basics/COVID/Data_Collection/Data/covid_allstates_history.csv','r') as rf:
    csv_reader=csv.reader(rf)
    header=next(csv_reader)
    print (header)