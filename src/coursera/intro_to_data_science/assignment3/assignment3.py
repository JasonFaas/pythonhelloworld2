


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

print("A3:" + str(type(answer_three())) + " average GDP over the last 10 years for each country")

def answer_four():
    Top15 = answer_one()
    columns_to_keep = [
        '2006',
        '2007',
        '2008',
        '2009',
        '2010',
        '2011',
        '2012',
        '2013',
        '2014',
        '2015'
    ]
    Top15 = Top15[columns_to_keep]
    Top15['mean_gdp'] = Top15.mean(axis=1)
    Top15['gdp_change'] = Top15['2015'] - Top15['2006']
    Top15 = Top15.sort_values('mean_gdp', ascending=False)
    # Top15['mean_gdp'][6]
    # print(Top15)

    return Top15['gdp_change'][5]

print("A4:" + str(answer_four()) + " By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP")


def answer_five():
    import pandas as pd
    import numpy as np
    Top15 = answer_one()
    # agg = Top15.agg({'Energy Supply per Capita': np.average})
    agg = Top15['Energy Supply per Capita'].mean()
    return agg

print("A5:" + str(answer_five()) + " mean Energy Supply per Capita")


def answer_six():
    Top15 = answer_one()
    idxmax = Top15['% Renewable'].idxmax()
    # print(str(idxmax) + " ")
    value2 = Top15['% Renewable'][idxmax]
    # print(str(value2) + " ")
    return (idxmax, value2)

print("A6:" + str(answer_six()) + " maximum % Renewable and what is the percentage")


def answer_seven():
    Top15 = answer_one()
    Top15['citations_ratio'] = Top15['Self-citations'] / Top15['Citations']
    idxmax = Top15['citations_ratio'].idxmax()
    value2 = Top15['citations_ratio'][idxmax]
    return (idxmax, value2)

print("A7:" + str(answer_seven()) + " Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio")


def answer_eight():
    Top15 = answer_one()
    Top15['est_pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15 = Top15.sort_values('est_pop', ascending=False)
    return Top15.head(3)['est_pop'].index[2]

print("A8:" + str(answer_eight()) + " Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?")

def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    corr = Top15['Energy Supply per Capita'].corr(Top15['Citable docs per Capita'])
    # print(corr)
    return corr

print("A9:" + str(answer_nine()) + " Pearson correlation for Energy Supply per Capita vs. Citable docs per Capita")


def plot9():
    import matplotlib.pyplot as plt

    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
    # plt.show()

plot9()

def answer_ten():
    import numpy as np
    import pandas as pd
    Top15 = answer_one()
    averageRenew = Top15['% Renewable'].mean()
    Top15['aboveBelow'] = Top15['% Renewable'] > averageRenew
    Top15['aboveBelow'] = Top15['aboveBelow'].replace(False, int(0))
    Top15['aboveBelow'] = Top15['aboveBelow'].replace(True, int(1))
    Top15['aboveBelow'] = Top15['aboveBelow'].astype(np.int64)

    aboveBelow = pd.Series(Top15['aboveBelow'].values, index=Top15.index.values)
    # aboveBelow.astype(np.int64)

    return aboveBelow

# print("A10:" + str(answer_ten()) + " Rank series % renewable")


def answer_thirteen():
    import numpy as np
    import pandas as pd
    Top15 = answer_one()
    Top15['est_pop'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['est_pop_comma'] = Top15['est_pop'].astype(str)
    # repl = lambda m: add_commas_to_float_as_string(m.group(0))
    repl = lambda m: "{:,}".format(float(m.group(0)))
    Top15['est_pop_comma'] = Top15['est_pop_comma'].str.replace(r'.*', repl)
    PopEst = pd.Series(Top15['est_pop_comma'].values, index=Top15.index.values)
    return PopEst


print("A13:" + str(answer_thirteen()) + " what")
