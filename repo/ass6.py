import pandas as pd
#ques1
dates = ['2025-06-25', '2025-06-26', '2025-06-27']
date_series = pd.to_datetime(dates)
df = pd.DataFrame({'Value': [1,2, 3]}, index=date_series)
print(df)

#ques2
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Marks': [80, 72, 85]})
result = pd.merge(df1, df2, on='ID', how='inner')
print(result)

result = pd.merge(df1, df2, on='ID', how='left')
print(result)

result = pd.merge(df1, df2, on='ID', how='right')
print(result)

res = df1.join(df2,rsuffix="_right",lsuffix="_left")
print(res)

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['A', 'B', 'C'],'dept':['HR','Sales','HR']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Marks': [80, 72, 85],'dept':['Sales','HR','IT']})
result = pd.merge(df1, df2, on=['ID', 'dept'], how='inner')
print(result)

#ques3
res = pd.concat([df1, df2], ignore_index=True)

df3 = pd.DataFrame({'ID':[3,4,5],'Score':[50,30,10],'s_id':['s1','s2','s3']})
final_df = pd.merge(res, df3, on='ID', how='inner')
print(final_df)
