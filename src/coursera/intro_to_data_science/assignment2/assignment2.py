import pandas as pd


def hello_world():
    return "Hello World!"


print(hello_world())


df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#'+col[1:]}, inplace=True)


names_ids = df.index.str.split('\s\(')  # split the index by '('

df.index = names_ids.str[0]  # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


def answer_one():
    return df['Gold'].idxmax()


print(answer_one() + "\t:The country with the most summer gold medals")


def answer_two():
    df['Summer_Gold_Minus_Winter_Gold'] = df['Gold'] - df['Gold.1']
    #print("HELPER:" + str(df.head()))
    #gold_min_country = df['Summer_Gold_Minus_Winter_Gold'].idxmin()
    #gold_Min_Helper = df.loc[gold_min_country]
    #print("HELPER:" + str(gold_min_country) + ":" + str(gold_Min_Helper))
    return df['Summer_Gold_Minus_Winter_Gold'].idxmax()


print(answer_two() + "\t:The country with the largest difference in summer and winter gold medal counts")


def answer_three():
    df_a3 = df.copy()
    only_gold_summer = df_a3.where(df_a3['Gold'] > 0)
    only_gold_summer.dropna(inplace=True)
    only_gold_both = only_gold_summer.where(df_a3['Gold.1'] > 0)
    only_gold_both.dropna(inplace=True)
    only_gold_both['summer_minus_winter_all_over_total'] = (only_gold_both['Gold'] - only_gold_both['Gold.1']) / (only_gold_both['Gold'] + only_gold_both['Gold.1'])

    #print("HELPER:" + str(only_gold_summer['Gold'].count()))
    #print("HELPER:" + str(only_gold_winter['Gold'].count()))
    #print("HELPER:" + str(only_gold_both['Gold'].count()))
    #print("HELPER:" + str(df_a3['Gold'].count()))
    return only_gold_both['summer_minus_winter_all_over_total'].idxmax()


print(answer_three() + "\t\t\t:The country with the largest proportional summer and winter difference")


def answer_four():
    Points = df.copy()
    Points['Points'] = Points['Gold.2'] * 3 + Points['Silver.2'] * 2 + Points['Bronze.2']
    Points.drop('Summer_Gold_Minus_Winter_Gold', axis=1, inplace=True)
    Points.drop('ID', axis=1, inplace=True)
    Points.drop('# Games', axis=1, inplace=True)
    Points.drop('# Summer', axis=1, inplace=True)
    Points.drop('Gold', axis=1, inplace=True)
    Points.drop('Silver', axis=1, inplace=True)
    Points.drop('Bronze', axis=1, inplace=True)
    Points.drop('Total', axis=1, inplace=True)
    Points.drop('# Winter', axis=1, inplace=True)
    Points.drop('Gold.1', axis=1, inplace=True)
    Points.drop('Silver.1', axis=1, inplace=True)
    Points.drop('Bronze.1', axis=1, inplace=True)
    Points.drop('Total.1', axis=1, inplace=True)
    Points.drop('Gold.2', axis=1, inplace=True)
    Points.drop('Silver.2', axis=1, inplace=True)
    Points.drop('Bronze.2', axis=1, inplace=True)
    Points.drop('Combined total', axis=1, inplace=True)
    # Points = Points.iloc[:,:]
    # print("HELPER874:\t\t" + str(Points['Points'].values))
    # print("HELPER874:\t\t" + str(Points.index.values))
    Points = pd.Series(Points['Points'].values, index=Points.index.values)
    # print("HELPER874:\t\t" + str(type(Points)))

    return Points


print(str(answer_four().head()) + "\n\t\t:The series which weights the Medals for each country")
