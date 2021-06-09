from dataFetch import covidcsvdatafetch
from cleanData import dropCsvColumns

covidcsvdatafetch.fetchDailyCovid()
dropCsvColumns.trimCovidDataColumns()

