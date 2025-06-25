import pandas as pd
a = [1,7,2]
var = pd.Series(a)
print(var)

data_set = {
    'fruits':["A","B","C"],
    'passing':[3,6,1]
}
data = pd.DataFrame(data_set)
print(data)

print(pd.__version__)
my_var = pd.Series(a,index=["x","y","z"])
print(my_var)
print(my_var["y"])

print(var.tolist())
print(type(var.tolist()))

print(data.loc[2])
print(data.loc[0:1])

Data = {
    'q' :[11,20,3],
    'd':[4,9,2]
}
df = pd.DataFrame(Data,index=["d1","d2","d3"])
print(df)
df.index = [100,200,300]
print(df)
result = df.columns
print(result)

r = df.loc[:,'q']
print(r)

d = [
    ['a','b'],['c','d'],['e','f'],['g','h']
]
df1 = pd.DataFrame(d,columns=['c1','c2'])
print(df1)
res = df1.iloc[1:3,:]
print(res)

df = pd.DataFrame({'A': [1, 2, 3, 4, 5],'B': [4, 5, 6, 7, 8],'C': [0, 10, 11, 12, 13]}, index=['r1', 'r2', 'r3', 'r4', 'r5'])
print(df)
result = df.drop(['r1','r3'])
res = df[df['C'] != 0]
print(result)
print(res)