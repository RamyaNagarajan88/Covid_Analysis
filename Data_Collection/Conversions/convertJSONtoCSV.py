import json
import csv

with open('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/Data/populationCensus.json','r') as jsonFile:
    jsonContent=json.load(jsonFile)
   
    with open('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/Data/populationCensus.csv','w', newline='') as csvFile:
        csvWriter=csv.writer(csvFile)
        isHeader=True
        for line in jsonContent:
            if isHeader:
                csvWriter.writerow(line.keys())
                isHeader=False
            csvWriter.writerow(line.values())   

 
   