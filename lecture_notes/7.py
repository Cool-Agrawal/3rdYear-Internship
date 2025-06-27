

import pandas as pd
import numpy as np
from pandas import value_counts
from pandas.core.interchange.dataframe_protocol import DataFrame


data = {'Col1':[3,np.nan, np.nan,2], 'Col2':[1.0,pd.NA,pd.NA,2.3]}
df = pd.DataFrame(data)
print(df)
f = df.fillna('-')
print(f)

df = pd.DataFrame([{1,2,3},{7,8,9},{12,13,14}],index=('a','b','c'),columns=('one','two','three'))
'''df = df.reindex(['a','b','c','d','e']).fillna('?')
df = df.reindex(['a','b','c','d','e']).ffill()
df = df.reindex(['a','b','c','d','e']).bfill()'''

df = df.reindex(['a','b','d','e','f'])
r = df.ffill(limit = 1)
#print(r)

data = {'Col1':[3,7,9,2,3], 'Col2':[12.5,1.0,11.3,7.4,2.3]}
df = pd.DataFrame(data)
res = df.replace({7:4,9:5})
#print(res)


df = pd.DataFrame(["$40,000","$40,000 Conditions"],columns=['P'])
df['P'] = df['P'].str.replace(r'\D+',"",regex = 'True').astype("int")
print(df)

#g = df.groupby(['Col1'])['Col2']
#print(g)

data = {'Col1':[3,7,9,2,4], 'Col2':[12.5,1.0,11.3,7.4,2.3],'Col3':['a','b','c','d','e']}
df = pd.DataFrame(data)
r = df.groupby(["Col1","Col3"])["Col2"].sum()
v = df.sort_values(by=['Col2','Col3'],ascending=[True,False])
#print(r)
print(v)
s = df.sort_values(by=['Col2'],inplace=True)
print(df)
z = df.sort_index(axis=1)
print(z)


print(pd.date_range("16/1/2025",periods=5))

df = pd.read_csv('../customers-100.csv')
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.index)
filtered = df[df['Company']>"a"]
print(filtered)

print(df["First Name"].value_counts())
pd.options.display.max_rows = 2
df = pd.read_csv('../customers-100.csv')
print(df)
n= df.dropna(inplace= True)
#print(n.to_string())
x = df['Index'].mean()
df.fillna({'Index':x},inplace=True)
