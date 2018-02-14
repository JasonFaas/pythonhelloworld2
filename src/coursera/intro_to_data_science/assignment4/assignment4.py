import pandas as pd

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


def hello_world():
    return "Hello World!"


print(hello_world())


census_df = pd.read_csv('census.csv')
#census_df.head()


def answer_five():
    census_df_a5 = census_df.copy()
    # print(str(census_df_a5['SUMLEV'].unique()))
    census_df_a5.where(census_df_a5['SUMLEV'] == 50, inplace=True)
    columns_to_keep = ['STNAME', 'CTYNAME']
    #print("HELPER:\t" + str(census_df_a5['CTYNAME'].count()))
    census_df_a5.dropna(inplace=True)
    #print("HELPER:\t" + str(census_df_a5['CTYNAME'].count()))
    census_df_a5 = census_df_a5[columns_to_keep]
    # print("HELPER:\n" + str(census_df_a5.head()))

    countStuff = census_df_a5.groupby(by=['STNAME']).count()
    # print("HELPER:\t\t" + str(countStuff))

    return countStuff['CTYNAME'].idxmax()


print(str(answer_five()) + "\t\t:The state with the most counties")


def answer_six():
    census_df_a6 = census_df.copy()
    census_df_a6.where(census_df_a6['SUMLEV'] == 50, inplace=True)
    census_df_a6.dropna(inplace=True)
    columns_to_keep = ['STNAME', 'CENSUS2010POP']
    census_df_a6 = census_df_a6[columns_to_keep]
    census_df_a6.sort_values(columns_to_keep, ascending=False, inplace=True)
    # print("HELPER:\n" + str(census_df_a6.head(8)))
    top_3_counties_each_state = census_df_a6.groupby('STNAME').head(3)
    top_3_total_each_state = top_3_counties_each_state.groupby(by=['STNAME']).sum()

    top_3_states_by_county_size_df = top_3_total_each_state.sort_values(['CENSUS2010POP'], ascending=False, inplace=False).head(3)
    # print("HELPER123:\n" + str(top_3_states_by_county_size_df))
    top_3_as_list = top_3_states_by_county_size_df.index.values
    # print("HELPER456:\n" + str(top_3_as_list))
    # print("HELPER:\n" + str(census_df_a6.groupby('STNAME').head(3).head(12)))

    #print("HELPER765:\t\t" + str(type(list(top_3_as_list))))

    return list(top_3_as_list)


print(str(answer_six()) + "\t\t:The 3 states with the 3 largest counties")


def answer_seven():
    census_df_a7 = census_df.copy()
    census_df_a7.where(census_df_a7['SUMLEV'] == 50, inplace=True)
    census_df_a7.dropna(inplace=True)
    columns_to_keep = [
        'STNAME',
        'CTYNAME',
        'POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015'
        ]
    census_df_a7 = census_df_a7[columns_to_keep]
    census_df_a7['max_pop_est'] = census_df_a7.max(axis=1)
    census_df_a7['min_pop_est'] = census_df_a7.min(axis=1)
    census_df_a7['abs_diff_est'] = census_df_a7['max_pop_est'] - census_df_a7['min_pop_est']
    idxmax_diff = census_df_a7['abs_diff_est'].idxmax()

    # print("HELPER432:\t" + str(census_df_a7.head(8)))
    return census_df_a7.loc[idxmax_diff]['CTYNAME']


print(str(answer_seven()) + "\t\t:The county with the largest fluctuation during 2010 through 2015")


def answer_eight():
    census_df_a8 = census_df.copy()
    census_df_a8.where(census_df_a8['SUMLEV'] == 50, inplace=True)
    census_df_a8.dropna(inplace=True)
    census_df_a8.where(census_df_a8['REGION'] != 3, inplace=True)
    census_df_a8.dropna(inplace=True)
    census_df_a8.where(census_df_a8['REGION'] != 4, inplace=True)
    census_df_a8.dropna(inplace=True)
    census_df_a8 = census_df_a8[census_df_a8['CTYNAME'].str.contains("Washington", na=False)]
    census_df_a8.where(census_df_a8['POPESTIMATE2015'] > census_df_a8['POPESTIMATE2014'], inplace=True)
    census_df_a8.dropna(inplace=True)
    columns_to_keep = [
        'STNAME',
        'CTYNAME'
    ]
    census_df_a8 = census_df_a8[columns_to_keep]
    # print("HELPER243:\t\t" + str(census_df_a8))
    return census_df_a8


print(str(answer_eight()) + "\t\t:5x2 df")

