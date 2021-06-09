import csv
import urllib.request as request


def fetchDailyCovid():
    siteurl="https://covidtracking.com/api/v1/states/daily.csv"
    with open('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/Data/covidhistorydata.csv','wb') as wf:
        with request.urlopen(siteurl) as response:
            source=response.read()
            wf.write(source)


