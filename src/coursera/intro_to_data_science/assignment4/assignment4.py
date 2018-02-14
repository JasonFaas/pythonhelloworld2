import pandas as pd

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


def hello_world():
    return "Hello World!"


print(hello_world())


# census_df = pd.read_csv('university_towns.txt')
#census_df.head()


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    f = open('university_towns.txt', 'r')
    message = f.read()
    f.close()
    split = message.split('\n')

    print(len(split))

    df = pd.DataFrame(columns=["State", "RegionName"])
    state = 'what'
    for city_or_state in split:
        if str.strip(city_or_state).endswith('[edit]'):
            state = str.strip(city_or_state)
            state = state[0:state.index('[')]
            # print(state)
        elif city_or_state.__contains__(" ("):
            city = city_or_state[0:city_or_state.index(" (")]
            df = df.append(pd.DataFrame([ [state, city]],columns=["State", "RegionName"]))

        # else:
            # print("Subcontext::" + city_or_state)

    # df

    # what_df = pd.DataFrame([["Michigan", "Ann Arbor"]],
    # columns=["State", "RegionName"])
    # what_df.
    # what_df.append(["Michigan", "Yipsilanti"] )


    return df

print("A1:" + str(get_list_of_university_towns().head()))