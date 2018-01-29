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
    return "YOUR ANSWER HERE"


print(str(answer_six()) + "\t\t:")