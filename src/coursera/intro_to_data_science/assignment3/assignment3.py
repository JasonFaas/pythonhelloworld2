import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


def hello_world():
    return "Hello World!"


print(hello_world())


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


def updateCountry(param):
    print(type(param))
    param = param[0:param.find('(')]

    return param.strip()


# energy['Country'] = updateCountry(energy['Country'])
energy['Country'] = energy['Country'].replace("Republic of Korea", "South Korea")
energy['Country'] = energy['Country'].replace("United States of America", "United States")
energy['Country'] = energy['Country'].replace("United Kingdom of Great Britain and Northern Ireland", "United Kingdom")
energy['Country'] = energy['Country'].replace("China, Hong Kong Special Administrative Region", "Hong Kong")
energy['Country'] = energy['Country'].str.replace(r'\d+', '')
energy['Country'] = energy['Country'].str.replace(r'\(.*\)', '')
energy['Country'] = energy['Country'].str.strip()
print(energy)
#index_col=0, skiprows=1)

# for col in energy.columns:
#     if col[:2] == '01':
#         energy.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
#     if col[:2] == '02':
#         energy.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
#     if col[:2] == '03':
#         energy.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
#     if col[:1] == '№':
#         energy.rename(columns={col: '#' + col[1:]}, inplace=True)
#
# names_ids = energy.index.str.split('\s\(')  # split the index by '('
#
# energy.index = names_ids.str[0]  # the [0] element is the country name (new index)
# energy['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)
#
# energy = energy.drop('Totals')
# energy.head()
#
#
# def answer_one():
#     return energy['Gold'].idxmax()
#
#
# print(answer_one() + "\t:The country with the most summer gold medals")
