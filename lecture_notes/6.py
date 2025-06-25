import pandas as pd
data = {
    'a':[1,2,3],
    'b':[10,20,30]
}
df = pd.DataFrame(data)
print(df)
print(df+2.7)
print(df-1)
print(df*3)
print(df//2)
df['c'] = df['a'] + df['b']
print(df)

df1 = pd.DataFrame({'a':[1,2,3,4],'b':[4,5,6,7]})
df2 = pd.DataFrame({'a':[12,13,14],'b':[10,20,30]},index=(1,2,3))
print(df1)
print(df2)
print("Addition is : ",df1+df2)
print("Sub",df1-df2)
print("Mul",df1*df2)
print("div",df1//df2)

d1 = pd.DataFrame({'Name':['a','b','c'],'sub':['s1','s2','s3'],'mark':[100,92,71]})
d2 = pd.DataFrame({'Name':['a','b','c'],'sub':['s31','s2','s3'],'mark':[10,9,1]})
res = pd.concat([d1,d2],keys={'a','b'},ignore_index='True')
r = pd.concat([d1,d2],axis=1)
print(res)
print(r)

result = d1.merge(d2,on= ('Name','sub'))
print(result)
r = d1.merge(d2,on = 'sub',how="outer")
print(r)
res = d1.join(d2,rsuffix="_right",lsuffix="_left")
print(res)

df = pd.DataFrame({'Col1':range(12),'Col2':['A','A','A','B','B','B','C','C','C','D','D','D'],
                  "data": pd.to_datetime(["2025-06-27","2025-06-11","2025-06-24"]*4)})
print(df)
result = df.pivot(index = "data",columns = "Col1",values="Col1")
print(result)

data = {
    'name':[1,2,3],
    'age':[2,3,4],
    'stu':['s1','s1','s3']
}
df = pd.DataFrame(data)
#print(df)
pivot_df = df.pivot_table(
    values="name",
    index="age",
    columns="stu",
    aggfunc="sum"
)
print(pivot_df)


