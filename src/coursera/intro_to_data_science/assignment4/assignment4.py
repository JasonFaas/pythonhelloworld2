import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


def hello_world():
    return "Hello World!"


print(hello_world())



def get_region_info():
    columns_to_keep = ['RegionID','RegionName','State','Metro','CountyName']
    region_info = pd.read_csv('City_Zhvi_AllHomes.csv')
    region_info = region_info[columns_to_keep]

    repl = lambda m: states.get(m.group(0))
    region_info['State'] = region_info['State'].str.replace(r'.*', repl)

    # print(city_and_region_verifier("AL", "Auburn", census_df))
    # print(city_and_region_verifier("AL", "whatwhatwhat", census_df))
    # print(city_and_region_verifier("KA", "Auburn", census_df))
    return region_info


def city_and_region_verifier(state, region_name, region_info):
    city_info = region_info.loc[region_info['RegionName'] == region_name]
    full_boolean = len(city_info.loc[city_info['State_Full'] == state]) == 1
    return full_boolean


# print("A0:" + str(get_region_info().head()))


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    # region_info = get_region_info()

    f = open('university_towns.txt', 'r')
    message = f.read()
    f.close()
    split = message.split('\n')

    # print(len(split))

    df = pd.DataFrame(columns=["State", "RegionName"])
    state = 'what'
    counter = 0
    for city_or_state in split:
        if str.strip(city_or_state).endswith('[edit]'):
            state = str.strip(city_or_state)
            state = state[0:state.index('[')]
            # print(state)
        elif len(city_or_state) > 5:
            city = city_or_state
            if city.__contains__(" ("):
                city = city[0:city_or_state.index(" (")]
            # if city.__contains__(','):
                # print("WHAT::" + city)
                # city = city[0:city.index(",")]
            # else:

            # if city_and_region_verifier(state, city, region_info):
                # print("WHERE:" + city + "::" + state + "::" + city_or_state)
            # else:
            df.loc[counter] = [state, city]
            counter += 1
        # else:
        #     print("Subcontext::" + city_or_state)

    # print(len(df))
    return df

print("A1:" + str(get_list_of_university_towns().head()))


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''

    energy = pd.read_excel(
        'gdplev.xls',
        sheet_name='Sheet1',
        skiprows=219,
        usecols=[4, 6],
        names=['Quarter', 'GDP_2009_Chained_Billions']
    )
    energy['next_negative'] = (energy[['GDP_2009_Chained_Billions']] <= energy[['GDP_2009_Chained_Billions']].shift()).any(axis=1)
    energy['next_positive'] = (energy[['GDP_2009_Chained_Billions']] > energy[['GDP_2009_Chained_Billions']].shift()).any(axis=1)
    energy['start_rec'] = (energy[['next_negative']] & energy[['next_negative']].shift(-1)).any(axis=1)
    energy['stop_rec'] = (energy[['next_positive']] & energy[['next_positive']].shift()).any(axis=1)
    # print(energy.head(20))

    # print(energy.head())
    for index, row in energy.iterrows():
        if row.start_rec:
            return_quarter = row.Quarter
            break

    return return_quarter

print("A2:" + str(get_recession_start()))


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''

    energy = pd.read_excel(
        'gdplev.xls',
        sheet_name='Sheet1',
        skiprows=219,
        usecols=[4, 6],
        names=['Quarter', 'GDP_2009_Chained_Billions']
    )
    energy['next_negative'] = (energy[['GDP_2009_Chained_Billions']] <= energy[['GDP_2009_Chained_Billions']].shift()).any(axis=1)
    energy['next_positive'] = (energy[['GDP_2009_Chained_Billions']] > energy[['GDP_2009_Chained_Billions']].shift()).any(axis=1)
    energy['start_rec'] = (energy[['next_negative']] & energy[['next_negative']].shift(-1)).any(axis=1)
    energy['stop_rec'] = (energy[['next_positive']] & energy[['next_positive']].shift()).any(axis=1)

    return_quarter = '2001q1'
    recession_started = False
    for index, row in energy.iterrows():
        if row.start_rec and not recession_started:
            recession_started = True
        if recession_started and row.stop_rec:
            return_quarter = row.Quarter
            break

    return return_quarter

print("A3:" + str(get_recession_end()))


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''

    energy = pd.read_excel(
        'gdplev.xls',
        sheet_name='Sheet1',
        skiprows=219,
        usecols=[4, 6],
        names=['Quarter', 'GDP_2009_Chained_Billions']
    )
    energy['next_negative'] = (
            energy[['GDP_2009_Chained_Billions']] <= energy[['GDP_2009_Chained_Billions']].shift()).any(axis=1)
    energy['next_positive'] = (
            energy[['GDP_2009_Chained_Billions']] > energy[['GDP_2009_Chained_Billions']].shift()).any(axis=1)
    energy['start_rec'] = (energy[['next_negative']] & energy[['next_negative']].shift(-1)).any(axis=1)
    energy['stop_rec'] = (energy[['next_positive']] & energy[['next_positive']].shift()).any(axis=1)

    return_quarter = '2001q1'
    low_gdp = 20 * 1000
    recession_started = False
    for index, row in energy.iterrows():
        if row.start_rec and not recession_started:
            recession_started = True
        if recession_started and row.stop_rec:
            break
        if recession_started:
            # print(low_gdp)
            billions_ = row['GDP_2009_Chained_Billions']
            if billions_ < low_gdp:
                low_gdp = billions_
                return_quarter = row.Quarter
            # print(str(row.Quarter) + ":" + str(billions_))

    return return_quarter


print("A4:" + str(get_recession_bottom()))


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    columns_to_keep = [
        'RegionID',
        'RegionName',
        'State',
        'Metro',
        'CountyName',
        "SizeRank"
    ]
    columns_to_keep_v2 = [
    ]
    region_info = pd.read_csv('City_Zhvi_AllHomes_old.csv')
    repl = lambda m: states.get(m.group(0))
    region_info['State'] = region_info['State'].str.replace(r'.*', repl)
    for year in range(2000, 2016, 1):
        for month in range(1, 13, 1):
            columns_to_keep.append(str(year) + "-" + str(month).zfill(2))
    for year in range(2016, 2017, 1):
        for month in range(1, 9, 1):
            columns_to_keep.append(str(year) + "-" + str(month).zfill(2))
    for year in range(2000, 2016, 1):
        for quarter in range(1, 5, 1):
            columns_to_keep_v2.append(str(year) + "q" + str(quarter))
    for year in range(2016, 2017, 1):
        for quarter in range(1, 4, 1):
            columns_to_keep_v2.append(str(year) + "q" + str(quarter))

    region_info = region_info[columns_to_keep]
    region_info = region_info.set_index(["State","RegionName"])
    # region_info = region_info.dropna()

    for year in range(2000, 2016, 1):
        for quarter in range(1, 5, 1):
            quarter_str = str(year) + "q" + str(quarter)
            first_month = str(year) + "-" + str((quarter - 1) * 3 + 1).zfill(2)
            second_month = str(year) + "-" + str((quarter - 1) * 3 + 2).zfill(2)
            third_month = str(year) + "-" + str((quarter - 1) * 3 + 3).zfill(2)
            region_info[quarter_str] = region_info[[first_month, second_month, third_month]].mean(axis=1)
    for year in range(2016, 2017, 1):
        for quarter in range(1, 3, 1):
            quarter_str = str(year) + "q" + str(quarter)
            first_month = str(year) + "-" + str((quarter - 1) * 3 + 1).zfill(2)
            second_month = str(year) + "-" + str((quarter - 1) * 3 + 2).zfill(2)
            third_month = str(year) + "-" + str((quarter - 1) * 3 + 3).zfill(2)
            region_info[quarter_str] = region_info[[first_month, second_month, third_month]].mean(axis=1)

    for year in range(2016, 2017, 1):
        for quarter in range(3, 4, 1):
            quarter_str = str(year) + "q" + str(quarter)
            first_month = str(year) + "-" + str((quarter - 1) * 3 + 1).zfill(2)
            second_month = str(year) + "-" + str((quarter - 1) * 3 + 2).zfill(2)
            region_info[quarter_str] = region_info[[first_month, second_month]].mean(axis=1)

    region_info = region_info[columns_to_keep_v2]

    # print(region_info[['2000q1', '2000-01', '2000-02', '2000-03']])

    # region_info = region_info[~region_info.index.duplicated(keep=False)]

    # print(region_info.loc["Texas"].loc["Austin"].loc["2010q3"])

    return region_info


# quarters = convert_housing_data_to_quarters()
# print("A5:" + str(quarters.head()))



def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''

    all_housing_data = convert_housing_data_to_quarters()
    found_start = False
    found_end = False
    bottom = get_recession_bottom()
    save_column = []
    start = get_recession_start()
    for columns in all_housing_data:
        if columns == start:
            found_start = True

        if found_start and not found_end:
            save_column.append(columns)

        if columns == bottom:
            found_end = True
    # print(save_column)
    all_housing_data = all_housing_data[save_column]
    all_housing_data = all_housing_data.dropna()
    # REALLY DROPPING NA ????????????????????????????????????????????????
    towns = get_list_of_university_towns()
    towns = towns.set_index(["State","RegionName"])
    # print(towns)

    towns_merged = pd.merge(all_housing_data, towns, how='inner', left_index=True, right_index=True)

    # df = pd.merge(all_housing_data, towns_merged, on=["State","RegionName"], how='outer', indicator=True)
    not_towns = pd.concat([all_housing_data, towns_merged]).drop_duplicates(keep=False)
    # print(towns_merged)
    #
    # print(len(all_housing_data))
    # print(len(towns_merged) + len(not_towns))
    # print(len(towns_merged))
    # print(len(towns))
    # print(len(not_towns))
    towns_merged['price_ratio'] = towns_merged[start]/towns_merged[bottom]
    not_towns['price_ratio'] = not_towns[start]/not_towns[bottom]
    ind = ttest_ind(not_towns['price_ratio'], towns_merged['price_ratio'])
    # print(type(ind))
    # print(ind.pvalue)
    towns_merged_mean = towns_merged['price_ratio'].mean()
    # print(towns_merged_mean)
    not_towns_mean = not_towns['price_ratio'].mean()
    # print(not_towns_mean)
    better = 'what'
    if towns_merged_mean < not_towns_mean:
        better = 'university town'
    else:
        better = 'non-university town'

    return (ind.pvalue < 0.01, ind.pvalue, better)

print("A6:" + str(run_ttest()))