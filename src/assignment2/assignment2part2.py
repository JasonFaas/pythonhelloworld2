import pandas as pd

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


    return top_3_as_list


print(str(answer_six()) + "\t\t:The 3 states with the 3 largest counties")