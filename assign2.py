

import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()


def answer_zero():
    return df.iloc[0]
answer_zero()


def answer_one():
    return df['Gold'].idxmax()
answer_one()


def answer_two():
    return (df['Gold'] - df['Gold.1']).idxmax()
answer_two()


def answer_three():
    df_more = df[(df['Gold']>=1) & (df['Gold.1']) >=1]
    return (((df_more['Gold'])-(df_more['Gold.1']))/df_more['Gold.2']).abs().argmax()
answer_three()

def answer_four():
    df['Points'] = pd.Series((df['Gold.2']*3) + (df['Silver.2']*2) + df['Bronze.2'])
    return df['Points']
answer_four()



census_df = pd.read_csv('census.csv')
census_df.head()

def answer_five():
    return census_df.groupby(['STNAME']).sum()['COUNTY'].idxmax()
answer_five()

# Question 6

def answer_six():
    return census_df[census_df['SUMLEV']==50].groupby('STNAME')['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).nlargest(3).index.values.tolist()
answer_six()

def answer_seven():

    county_only = census_df[census_df['SUMLEV']==50].set_index('CTYNAME')
    years = ['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
    return (county_only.loc[:, years].max(axis=1) - county_only.loc[:, years].min(axis=1)).argmax()
answer_seven()



def answer_eight():


    region_county = census_df[(census_df['SUMLEV']==50) & ((census_df['REGION'] ==1) | (census_df['REGION'] ==2))]
    start_washington = region_county[region_county['CTYNAME'].str.startswith('Washington')]
    popestimate_comparison = start_washington[start_washington['POPESTIMATE2015']> start_washington['POPESTIMATE2014']]
    return popestimate_comparison[['STNAME','CTYNAME']]
answer_eight()
