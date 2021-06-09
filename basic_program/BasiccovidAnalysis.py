import json
#population data
with open('E:/Ramya/brush ups/Basics/COVID/Data_Collection/populationCensus.json','rb') as rf:
    populationData=json.load(rf)
for p in populationData:
   del p['rank'],p['Growth'],p['Pop2018'],p['Pop2010'],p['growthSince2010'],p['Percent'],p['density']

#state abbreviations data 
with open('E:/Ramya/brush ups/Basics/COVID/Data_Collection/stateAbbreviations.json','r') as rf:
    statenamesData=json.load(rf)
    for s in statenamesData:
        del s['Abbrev']

#adding state code to populationsdata
for p in populationData:
    for s in statenamesData:
        if  p['State']==s['State']:
            p['code']=s['Code']

#covid data
with open('E:/Ramya/brush ups/Basics/COVID/Data_Collection/cleaned_covid_allstates_current.json','r') as rf:
    covidData=json.load(rf)


#statewise ranking based on number of positive covids

covidPosRanking=sorted(covidData,key=lambda entry: entry['positiveCount'],reverse=True)
print(f'STATE   POSITIVE CASES')
for i in covidPosRanking:
    print (f"{i['state']} {i['positiveCount']}")


#per capita calculation

ignoreStates=["VI","GU","MP","AS"]

def calculatePerCapita(metric,name):
    for entry in covidData:
        if entry['state'] in ignoreStates:
            entry[name]= float(0) 
        else:
            for p in populationData: 
                if p['code']==entry['state']:
                    entry[name]=entry[metric]/p['Pop'] 

 
#positive cases per capita calculation

calculatePerCapita('positiveCount','posPerCapita')
covidPosPerCapita=sorted(covidData,key=lambda entry: entry['posPerCapita'],reverse=True)
print(f'STATE   PERCAPITA   COUNT for every 100,000 people ')
for i in covidPosPerCapita:
    print (f"{i['state']}   {round(i['posPerCapita'],5)} {round(i['posPerCapita']*100000,5)}")

# percent needing help and are hospitalized
print("Percent of covid patients hospitalised state wise")
for state in covidData:
    if state['positiveCount']!=0:
        print (f"{state['state']} {(state['hospitalizedCurrently']/state['positiveCount'])*100}")


        
            

