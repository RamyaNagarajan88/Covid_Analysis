import pandas as pd
import numpy as np
import datetime
from calendar import monthrange
import psycopg2

df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/Data/covidhistorydata.csv')


# fetching data from db
connection=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="mydb2020")
cur=connection.cursor()
sqlQuery='''select usstates.code, populationcensus.pop 
from usstates inner join populationcensus 
on usstates.state=populationcensus.state'''
cur.execute(sqlQuery)
popResult=cur.fetchall()
statesPop=dict(tuple(popResult))


#method to convert all integer/string dates to date type
def convertToDate(dateEntry):
    d=str(dateEntry).replace('/','')
    return (datetime.datetime.strptime(str(d),'%Y%m%d')).date()


#convert date column of dataframe from integer representation of date to date type
df['date']=df['date'].apply(convertToDate)



#get last dates of all months(for cummulative data)


def lastDataDates(year):
    #get start and end date of data collected
    df.sort_values(by=['date'],inplace=True, ascending=False)
    startDate=df['date'].iloc[-1]
    endDate=df['date'].iloc[0]
    for m in range(1,13):
        if startDate.month<=m<=endDate.month:
            endDay=monthrange(year,m)[1]
            checkDate= convertToDate(str(year)+str(m)+str(endDay))
            if checkDate<=endDate:
                checkDates.append(checkDate)
            else:
                checkDates.append(endDate)
    return checkDates
    
checkDates=[]        
checkDates=lastDataDates(2020)

def filterEnteries(stateCode,dateEntry,metric):
    storeDict={}
    filt=(df['state']==stateCode) & (df['date']==dateEntry)
    res=df.loc[filt,metric]
    storeDict['state']=stateCode
    storeDict['month']=dateEntry
    if(res.empty==False | res.dropna().empty==False):
        storeDict[metric+'Total']= int(float(res.to_string(index=False).strip(" ")))
    else:
        storeDict[metric+'Total']= 0
    return storeDict



def resultCalculations(stateCode,dateEntry,metric,prevMonthValue):
    
    resultDict= filterEnteries(stateCode,dateEntry,metric)  
    resultDict[metric+'PerCapita']=(resultDict[metric+'Total']/statesPop[stateCode])*100000
    resultDict[metric+'Increase']=resultDict[metric+'Total']-prevMonthValue
    resultDict[metric+'IncreasesPerCapita']=resultDict[metric+'Increase']/statesPop[stateCode]*100000
    try:
        resultDict[metric+'IncreasePercent']=(resultDict[metric+'Increase']/prevMonthValue)*100
    except ZeroDivisionError:
        resultDict[metric+'IncreasePercent']=0
    prevMonthValue= resultDict[metric+'Total']                 
    return resultDict,prevMonthValue

#collect for all states, positive counts and increase of each month 
def getMetricsData(metric):
    resultList=[]
    for state in statesPop.keys():
        prevMonthValue=0
        for d in checkDates:
            resultDict,prevMonthValue=resultCalculations(state,d,metric,prevMonthValue)
            resultList.append(resultDict)
    return resultList    

metrics=['positive','death','hospitalizedCumulative']

for m in metrics:
    resultDf=pd.DataFrame(getMetricsData(m))
    resultDf.set_index('state',inplace=True)
    fileName='E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/GrowthStateWiseResults/'+m+'CountStateWise.csv'
    resultDf.to_csv(fileName,float_format='%.f')

