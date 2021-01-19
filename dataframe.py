import pandas as pd
from regions import regions
from countries import countries

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

dataframe = pd.read_csv("https://covid19.who.int/WHO-COVID-19-global-data.csv", low_memory=False)
dataframe["Date_reported"] = pd.to_datetime(dataframe["Date_reported"])
dataframe = dataframe[dataframe['WHO_region'] != 'Other']
dataframe = dataframe[dataframe['New_cases'] >= 0]
dataframe['WHO_region'] = dataframe['WHO_region'].apply(lambda abbr:regions[abbr])
dataframe = dataframe.rename(columns={'WHO_region':'Region'})
dataframe["Country"].replace(countries, inplace=True)
