


def hello_world():
    return "Hello World!"


print(hello_world())


def answer_one():
    import pandas as pd
    # from pandas import ExcelWriter
    # from pandas import ExcelFile
    energy = pd.read_excel(
        'Energy Indicators.xls',
        sheet_name='Energy',
        skiprows=17,
        skip_footer=38,
        usecols=[2,3,4,5],
        names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
        na_values='...'
    )
    energy['Energy Supply'] *= 1000 * 1000
    energy['Country'] = energy['Country'].str.replace("Republic of Korea", "South Korea")
    energy['Country'] = energy['Country'].str.replace("United States of America", "United States")
    energy['Country'] = energy['Country'].str.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
    energy['Country'] = energy['Country'].str.replace("China, Hong Kong Special Administrative Region", "Hong Kong")
    energy['Country'] = energy['Country'].str.replace(r'\d+', '')
    energy['Country'] = energy['Country'].str.replace(r'\(.*\)', '')
    energy['Country'] = energy['Country'].str.strip()
    # print(energy)

    gdp = pd.read_csv('world_bank.csv', skiprows=4)
    gdp['Country Name'] = gdp['Country Name'].str.replace("Korea, Rep.", "South Korea")
    gdp['Country Name'] = gdp['Country Name'].str.replace("Iran, Islamic Rep.", "Iran")
    gdp['Country Name'] = gdp['Country Name'].str.replace("Hong Kong SAR, China", "Hong Kong")
    columns_to_keep = ['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    gdp = gdp[columns_to_keep]
    #print(gdp)

    ScimEn = pd.read_excel(
        'scimagojr-3.xlsx',
        sheet_name='Sheet1'
    )

    #print(ScimEn)

    ScimEn = ScimEn.set_index('Country')
    gdp = gdp.set_index('Country Name')
    energy = energy.set_index('Country')
    # print(len(ScimEn.index) - 162)
    # print(len(gdp.index) - 162)
    # print(len(energy.index) - 162)

    # print(energy)
    first2 = pd.merge(ScimEn, gdp, how='inner', left_index=True, right_index=True)
    all3 = pd.merge(first2, energy, how='inner', left_index=True, right_index=True)
    #print(all3)
    all3 = all3.sort_values('Rank')

    return all3.head(15)

# answer_one()
# print(str(answer_one()) + "all 3 merged")


def answer_two():
    import pandas as pd
    # from pandas import ExcelWriter
    # from pandas import ExcelFile
    energy = pd.read_excel(
        'Energy Indicators.xls',
        sheet_name='Energy',
        skiprows=17,
        skip_footer=38,
        usecols=[2,3,4,5],
        names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
        na_values='...'
    )
    energy['Energy Supply'] *= 1000 * 1000
    energy['Country'] = energy['Country'].str.replace("Republic of Korea", "South Korea")
    energy['Country'] = energy['Country'].str.replace("United States of America", "United States")
    energy['Country'] = energy['Country'].str.replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
    energy['Country'] = energy['Country'].str.replace("China, Hong Kong Special Administrative Region", "Hong Kong")
    energy['Country'] = energy['Country'].str.replace(r'\d+', '')
    energy['Country'] = energy['Country'].str.replace(r'\(.*\)', '')
    energy['Country'] = energy['Country'].str.strip()
    # print(energy)

    gdp = pd.read_csv('world_bank.csv', skiprows=4)
    gdp['Country Name'] = gdp['Country Name'].str.replace("Korea, Rep.", "South Korea")
    gdp['Country Name'] = gdp['Country Name'].str.replace("Iran, Islamic Rep.", "Iran")
    gdp['Country Name'] = gdp['Country Name'].str.replace("Hong Kong SAR, China", "Hong Kong")
    columns_to_keep = ['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    gdp = gdp[columns_to_keep]
    #print(gdp)

    ScimEn = pd.read_excel(
        'scimagojr-3.xlsx',
        sheet_name='Sheet1'
    )

    #print(ScimEn)

    ScimEn = ScimEn.set_index('Country')
    gdp = gdp.set_index('Country Name')
    energy = energy.set_index('Country')
    # print(len(ScimEn.index) - 162)
    # print(len(gdp.index) - 162)

    # print(energy)
    first2Outer = pd.merge(ScimEn, gdp, how='outer', left_index=True, right_index=True)
    all3Outer = pd.merge(first2Outer, energy, how='outer', left_index=True, right_index=True)

    first2 = pd.merge(ScimEn, gdp, how='inner', left_index=True, right_index=True)
    all3 = pd.merge(first2, energy, how='inner', left_index=True, right_index=True)

    return len(all3Outer.index) - len(all3)

# answer_two()
print("A2:" + str(answer_two()) + " Rows lossed")


def answer_three():
    import pandas as pd
    import numpy as np
    Top15 = answer_one()
    Top15['average'] = (Top15['2006'] + Top15['2007'] + Top15['2008'] + Top15['2009'] + Top15['2010'] + Top15['2011'] + Top15['2012'] + Top15['2013'] + Top15['2014'] + Top15['2015']) / 10
    # avgGDP = np.mean(Top15['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015'])
    
    
    avgGDP = pd.Series(Top15['average'].values, index=Top15.index.values)
    return avgGDP

print("A3:" + str(answer_three()) + " average GDP over the last 10 years for each country")


