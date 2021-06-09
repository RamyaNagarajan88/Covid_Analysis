import pandas as pd
#to display all rows
pd.set_option('display.max_rows',None)
#to read data
df=pd.read_csv('E:/Ramya/brush ups/Basics/CASE_STUDIES/COVID/Data_Collection/Data/covidhistorydata.csv')
#data = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')

# #to get shape of df
# print(df.shape)

# #to get df info
# print(df.info)

# #to get first 5 enteries
# print(df.head())

# #to get date column details-->series
# print(df['date'])

#boolean/logical expression
#print(df[(df['date']==20200706) & (df['state']=='TX')])

#to get row 2 values
# print(df.loc[2])
# print(df.iloc[2])
#print(df.columns)

#to get row 2 and column 'date&death values'
# print(df.loc[[2,5],['death','date']])

#to get slice of rows and columns
#print(df.loc[2:5,'death':'hospitalizedIncrease'])
#print(df.head)

#loc using boolean indexing
# print(df.loc[(df['date']==20200706) & (df['state']=='TX')])

# #print specific columns
# print(df.loc[(df['date']==20200706) & (df['state']=='TX'),['hospitalizedCumulative','positiveIncrease']])

#isin list
#datesList=[20200706,20200705,20200704]
#filt=df['date'].isin(datesList)
#print(df.loc[df['date'].isin(datesList)])

#str.contains(,fillna)
# filt=df['lastUpdateEt'].str.contains('/5/',na=False, regex=False)
# print(df.loc[filt,['state','death','lastUpdateEt']])

#to rename column name
#print (df.columns)
