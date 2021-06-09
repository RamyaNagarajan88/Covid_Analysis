import pandas as pd
from matplotlib import pyplot as plt 
import datetime


posDf=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/positiveCountStateWise.csv')
hosDf=pd.read_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/hospitalizedCumulativeCountStateWise.csv')
combDf=posDf[['state','month','positiveIncrease']].copy()
combDf['hospitalizedCumulativeIncrease']=hosDf['hospitalizedCumulativeIncrease']
combDf['month']=combDf['month'].map(lambda x:(datetime.datetime.strptime(x,'%Y-%m-%d').strftime('%B')))
combDf['posHosPercent']=round(((combDf['hospitalizedCumulativeIncrease']/combDf['positiveIncrease'])*100),3)
combDf.set_index('state',inplace=True)
combDf.to_csv('E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/positiveToHospitalRatio.csv')

# x=combDf.loc['AZ','month']
# y_pos=combDf.loc['AZ','positiveIncrease']
# y_hosp=combDf.loc['AZ','hospitalizedCumulativeIncrease']
# #print(plt.style.available)
# plt.plot(x,y_pos,label='positive increase')
# plt.plot(x,y_hosp,label='hospitalized increase')
# plt.xlabel("Month")
# plt.ylabel("Cases total")
# plt.xkcd()
# plt.grid()
# plt.legend()
# plt.show()


#two y axis
def plotGraph(stateCode,saveCopy):
    x=combDf.loc[stateCode,'month']
    y_pos=combDf.loc[stateCode,'positiveIncrease']
    fig,ax1=plt.subplots()
    color='tab:red'
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Cases count",color=color)
    ax1.plot(x,y_pos,label='positive increase',color=color)

    ax2=ax1.twinx()
    color='tab:blue'
    y_hosp=combDf.loc[stateCode,'hospitalizedCumulativeIncrease']
    ax2.set_ylabel("Cases count",color=color)
    ax2.plot(x,y_hosp,label='hospitalized increase',color=color)
    plt.xkcd()
    plt.grid()
    fig.tight_layout()
    fig.legend(loc="upper right")
    if saveCopy.lower()=='y':
        fileName='E:/Ramya/brushUps/Basics/CASE_STUDIES/COVID/Data_Analysis/'+stateCode+'posHospIncrease.png'
        plt.savefig(fileName)
    plt.show()

state=input("Enter the state code: ")
saveCopy=input("Do you want to save graph(y for yes and n for no): ")
plotGraph(str(state),str(saveCopy))