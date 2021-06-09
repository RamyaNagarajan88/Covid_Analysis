import psycopg2

connection=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="mydb2020")
cur=connection.cursor()
sqlQuery="""
    CREATE TABLE covidHistoryData(
    dataQualityGrade text,
    date integer,
    death integer,
    deathIncrease integer,
    fips text,
    hospitalizedCumulative integer,
    hospitalizedCurrently integer,
    hospitalizedIncrease integer,
    inIcuCumulative integer,
    inIcuCurrently integer,
    lastUpdateEt text,
    negative integer,
    negativeTestsViral integer,
    onVentilatorCumulative integer,
    onVentilatorCurrently integer,
    pending integer,
    positive integer,
    positiveCasesViral integer,
    positiveIncrease integer,
    positiveTestsViral integer,
    recovered integer,
    state text,
    totalTestResults integer,
    totalTestResultsIncrease integer,
    totalTestsViral integer,
    PRIMARY KEY(date,state)
)
"""
cur.execute(sqlQuery)
connection.commit()