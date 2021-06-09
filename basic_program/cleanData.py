import json
import urllib.request as request


# siteurl="https://covidtracking.com/api/v1/states/tx/20200630.json"
# with open('E:/Ramya/brush ups/Basics/COVID/covid_texas_0630.json','wb') as wf:
#     with request.urlopen(siteurl) as response:
#         source=response.read()
#         wf.write(source)

# siteurl="https://covidtracking.com//api/v1/states/current.json"
# with open('E:/Ramya/brush ups/Basics/COVID/covid_allstates_current.json','wb') as wf:
#     with request.urlopen(siteurl) as response:
#         source=response.read()
#         wf.write(source)



with open('E:/Ramya/brush ups/Basics/COVID/covid_allstates_current.json','rb') as rf:
    covid_data=json.load(rf)
    data=[]
    
    for entry in covid_data:
        details={}
        details['state']=entry['state']
        details['totalTests']=entry['totalTestsViral']
        details['positiveTestResults']=entry['positiveTestsViral']
        details['positiveCount']=entry['positive']
        details['positiveIncrease']=entry['positiveIncrease']
        details['negativeCount']=entry['negative']
        details['negativeTestResults']=entry['negativeTestsViral']
        details['hospitalizedCurrently']=entry['hospitalizedCurrently']
        details['hospitalizedIncrease']=entry['hospitalizedCurrently']
        details['inIcuCurrently']=entry['inIcuCurrently']
        details['onVentilatorCurrently']=entry['onVentilatorCurrently']
        details['deaths']=entry['death']
        details['deathIncrease']=entry['deathIncrease']
        details['recovered']=entry['recovered']
        data.append(details)
    
with open('E:/Ramya/brush ups/Basics/COVID/cleaned_covid_allstates_current.json','w') as wf:
    json.dump(data,wf)
        

        
        
       
        
        
        
        
        





