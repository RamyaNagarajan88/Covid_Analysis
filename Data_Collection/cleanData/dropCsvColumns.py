import pandas as pd

def trimCovidDataColumns():
    trimmedContents=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/Data/covidhistorydata.csv')
    trimmedContents.drop(['hash','commercialScore','negativeRegularScore','negativeScore','total','score','positiveScore','grade','posNeg','checkTimeEt','dateChecked','dateModified','hospitalized','negativeIncrease'],axis=1,inplace=True)

    #while writing to database
    # colReorder=['dataQualityGrade','date','death','deathIncrease','fips','hospitalizedCumulative','hospitalizedCurrently','hospitalizedIncrease','inIcuCumulative','inIcuCurrently','lastUpdateEt','negative','negativeTestsViral','onVentilatorCumulative','onVentilatorCurrently','pending','positive','positiveCasesViral','positiveIncrease','positiveTestsViral','recovered','state','totalTestResults','totalTestResultsIncrease','totalTestsViral']
    # cleanedData=trimmedContents.reindex(colReorder,axis=1)

    trimmedContents.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Collection/Data/covidhistorydata.csv',index=False,float_format='%.f')