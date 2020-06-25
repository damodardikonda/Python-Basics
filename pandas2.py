import pandas as pd;
import numpy as np
from io import StringIO, BytesIO

df=pd.read_csv('mercedesbenz.csv')

print(df.head())

print(df.info())

print(df.describe())

#Get the unique category counts
print(df['X0'].value_counts())

print(df[df['y']>100])

print(df.corr())

print(df['X11'].value_counts()_


lst_data=[[1,2,3],[3,4,np.nan],[5,6,np.nan],[np.nan,np.nan,np.nan]]df=pd.DataFrame(lst_data)

print(df.head())


print(df.dropna(axis=0))

df.dropna(axis=1)

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'],
                     columns=['one', 'two', 'three'])
print(df.head())


df2=df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

df2.dropna(axis=0)
print(pd.isna(df2['one']))
print(df2['one'].notna())

print(df2.fillna('Missing'))

print(df2['one'].values)



data = ('col1,col2,col3\n'
            'x,y,1\n'
            'a,b,2\n'
            'c,d,3')

print(type(data))

pd.read_csv(StringIO(data))


df=pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3'])
df.to_csv('Test.csv')
## Specifying columns data types

data = ('a,b,c,d\n'
            '1,2,3,4\n'
            '5,6,7,8\n'
            '9,10,11')

print(data)

df=pd.read_csv(StringIO(data),dtype=object)
print(df)

print(df['a'][1])

df=pd.read_csv(StringIO(data),dtype={'b':int,'c':np.float,'a':'Int64'})

print(df)

print(df['a'][1])

## check the datatype
print(df.dtypes)


## Index columns and training delimiters

data = ('index,a,b,c\n'
           '4,apple,bat,5.7\n'
            '8,orange,cow,10')

pd.read_csv(StringIO(data),index_col=0)


data = ('a,b,c\n'
           '4,apple,bat,\n'
            '8,orange,cow,')

pd.read_csv(StringIO(data))

pd.read_csv(StringIO(data),index_col=False)

## Combining usecols and index_col
 data = ('a,b,c\n'
           '4,apple,bat,\n'
            '8,orange,cow,')

pd.read_csv(StringIO(data), usecols=['b', 'c'],index_col=False)

## Quoting and Escape Characters¶. Very useful in NLP

data = 'a,b\n"hello, \\"Bob\\", nice to see you",5'

pd.read_csv(StringIO(data),escapechar='\\')


df=pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',
                 sep='\t')

print(df.head())
