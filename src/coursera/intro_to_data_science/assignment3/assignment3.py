import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


def hello_world():
    return "Hello World!"


print(hello_world())


def answer_one():
    energy = pd.read_excel(
        'Energy Indicators.xls',
        sheet_name='Energy',
        skiprows=17,
        skip_footer=38,
        usecols='C:F',
        names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
        na_values='...'
    )
    energy['Energy Supply'] *= 1000 * 1000
    energy['Country'] = energy['Country'].replace("Republic of Korea", "South Korea")
    energy['Country'] = energy['Country'].replace("United States of America", "United States")
    energy['Country'] = energy['Country'].replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
    energy['Country'] = energy['Country'].replace("China, Hong Kong Special Administrative Region", "Hong Kong")
    energy['Country'] = energy['Country'].str.replace(r'\d+', '')
    energy['Country'] = energy['Country'].str.replace(r'\(.*\)', '')
    energy['Country'] = energy['Country'].str.strip()
    #print(energy)

    gdp = pd.read_csv('world_bank.csv', skiprows=4)
    gdp['Country Name'] = gdp['Country Name'].replace("Korea, Rep.", "South Korea")
    gdp['Country Name'] = gdp['Country Name'].replace("Iran, Islamic Rep.", "Iran")
    gdp['Country Name'] = gdp['Country Name'].replace("Hong Kong SAR, China", "Hong Kong")
    columns_to_keep = ['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    gdp = gdp[columns_to_keep]
    #print(gdp)

    ScimEn = pd.read_excel(
        'scimagojr-3.xlsx',
        sheet_name='Sheet1'
    )

    ScimEn = ScimEn.head(15)
    #print(ScimEn)

    ScimEn = ScimEn.set_index('Country')
    gdp = gdp.set_index('Country Name')
    energy = energy.set_index('Country')
    # print(energy)
    first2 = pd.merge(ScimEn, gdp, how='inner', left_index=True, right_index=True)
    all3 = pd.merge(first2, energy, how='inner', left_index=True, right_index=True)
    #print(all3)

    return all3


print(str(answer_one()) + "all 3 merged")
