import pandas as pd
import psycopg2
import datetime
import time
from calendar import monthrange
from matplotlib import pyplot as plt


connection=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="mydb2020")
cur=connection.cursor()

def convertToDate(dateEntry):
    dateNewFormat=str(dateEntry).replace('-','')
    return (datetime.datetime.strptime(str(dateNewFormat),'%Y%m%d')).date()


def createDataFrames(usermetric):
    df=pd.DataFrame()
    if usermetric in range(1,10):
        df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/Data/covidhistorydata.csv')
    elif usermetric==10:
        df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/GrowthStateWiseResults/positiveCountStateWise.csv')
        df.rename(columns={'positiveIncrease':'positivesForMonth','month':'date'},inplace=True)
    elif usermetric==11:
        df=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/GrowthStateWiseResults/deathCountStateWise.csv')
        df.rename(columns={'deathIncrease':'deathsForMonth','month':'date'},inplace=True)
    df['date']=df['date'].apply(convertToDate)
    return df


def getEndDate(userMonth,dataEnd):
    if userMonth==dataEnd.month:
        return dataEnd
    else:
        endDay=monthrange(2020,userMonth)[1]
        return convertToDate(str(2020)+str(userMonth)+str(endDay))


def filterDataAndSort(df,metric,userMonth,dataEnd):

    sqlQuery_pop='''select usstates.code, populationcensus.pop 
    from usstates inner join populationcensus 
    on usstates.state=populationcensus.state'''
    cur.execute(sqlQuery_pop)
    popResult=cur.fetchall()
    statesPop=dict(tuple(popResult))

    filteredDf=pd.DataFrame()

    if 'PerCapita' in metric:
        knownMetric=metric.split('PerCapita')[0]
        for state in statesPop.keys():
            filt=(df['state']==state) & (df['date']==getEndDate(userMonth,dataEnd))
            filtDf=df.loc[filt,['state',knownMetric]]
            filtDf[metric]=(filtDf[knownMetric]/statesPop[state])*100000
            filteredDf=filteredDf.append(filtDf,ignore_index=True)
    else:
        for state in statesPop.keys():
            filt=(df['state']==state) & (df['date']==getEndDate(userMonth,dataEnd))
            filteredDf=filteredDf.append(df.loc[filt,['state',metric]],ignore_index=True)
    filteredDf.sort_values(by=[metric],inplace=True, ascending=False)
    return filteredDf.iloc[0:15]  
  

def showGraph(resDf,metric):

    sqlQuery_abbr='''select usstates.code, usstates.state from usstates'''
    cur.execute(sqlQuery_abbr)
    abbrResults=cur.fetchall()
    statesNames=dict(tuple(abbrResults))

    series_x=resDf['state']
    series_y=resDf[metric]
    x_axis=[]
    y_axis=[]
    for index,value in series_x.items():
        x_axis.append(statesNames[value])
    for index,value in series_y.items():
        y_axis.append(int(value))

    if 'PerCapita' in metric:
        plt.xlabel('Counts per 100000 people')
    else:
        plt.xlabel(metric+' Counts')

    x_axis.reverse()
    y_axis.reverse()

    for index, value in enumerate(y_axis):
        plt.text(value,index, str(value))

    plt.barh(x_axis,y_axis,height=0.5)
    plt.title('Top 15 states '+metric+' wise')
    plt.grid()
    plt.tight_layout()
    plt.xkcd()
    fileName='E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/TopStatesResults/'+metric+time.strftime('%Y%m%d')+'.png'
    plt.savefig(fileName)
    plt.show()



def main():

    metricsOptions='''
    1:Positive 
    2:Death 
    3:Recovered 
    4:Total Tests 
    5:Positive Increase per day
    6:Positive per capita
    7:Death per capita
    8.Recovered per capita
    9.Total tests per capita
    10.Positives cases per month
    11. Death cases per month
    '''
    metricsDict={1:'positive',
        2:'death',
        3:'recovered',
        4:'totalTestResults',
        5:'positiveIncrease',
        6:'positivePerCapita',
        7:'deathPerCapita',
        8:'recoveredPerCapita',
        9:'totalTestResultsPerCapita',
        10:'positivesForMonth', 
        11:'deathsForMonth'
        }
    
    print(metricsOptions)
    usermetric=int(input("Enter a number for metric: "))
    userMonth=int(input("Enter number value for month: "))

    df=createDataFrames(usermetric)
    df.sort_values(by=['date'],inplace=True, ascending=False)
    dataStart=(df['date'].iloc[-1])
    dataEnd=(df['date'].iloc[0])

    if dataStart.month<=userMonth<=dataEnd.month:
        metric=metricsDict[usermetric]
        resDf=filterDataAndSort(df,metric,userMonth,dataEnd)
        showGraph(resDf,metric)
        
    else:
        print("No data available for this month")



if __name__ == "__main__":
    main()