import json
import urllib.request as request

siteurl="https://covidtracking.com//api/v1/states/current.json"
with open('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/covid_allstates_current.json','wb') as wf:
    with request.urlopen(siteurl) as response:
        source=response.read()
        wf.write(source)