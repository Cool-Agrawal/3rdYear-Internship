#ques1
import pandas as pd
var = {'a':100,'b':200,'c':300}
data = pd.Series(var)
print(data)

my_list = [2,5,9,3,6]
d = pd.Series(my_list)
print(d)

data1 = pd.Series(var['a'])
print(data1)
d1 = d.iloc[2]
print(d1)

#ques2
data = [
    [1,"A",'a'],[2,"B",'b'],[3,"C",'c']
]
df = pd.DataFrame(data,columns=["no","fname","lname"])
print(df)

d = {
    'A':[12,60,3],
    'B':[4,9,18]
}
df1 = pd.DataFrame(d)
print(df1)

l = [
    [1,"list1",'a'],[2,"list2",'b'],[3,"list3",'c']
]
df = pd.DataFrame(l,columns=["no","list","name"])
print(df)

t = [
    (1,"tuple1",'a'),(2,"tuple2",'b'),(3,"tuple3",'c')
]
df = pd.DataFrame(t,columns=["no","tuple","name"])
print(df)

dic = [
    {"A":1,"B":2,"C":3},
    {"A":11,"B":22,"C":33},
    {"A":10,"B":20,"C":30}
]
df = pd.DataFrame(dic)
print(df)

#ques3
