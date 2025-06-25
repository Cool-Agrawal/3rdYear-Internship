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
d2 = pd.DataFrame({'Name':['ab','bc','cd'],'sub':['sub1','sub2','sub3'],'mark':[10,9,1]},index=(3,4,5))
res = pd.concat([d1,d2])
print(res)
