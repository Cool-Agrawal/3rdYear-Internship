
d = {1:"Python",2:"Program","name":"Hello",4:{1:"a",2:"b"}}
print(d["name"])
print(d[4])
print(d[4][1])
d[3] = "Programming"
d[5] = "Function"
print(d)
d2 = d.copy()
print(d2)
print(d.items())
print(d.keys())
print(d.values())
d.pop(1)
print(d)
d.popitem()
print(d)
d1 = {1:"hello",2:"world",3:"h",4:"i"}
d3 = {1:"hi",2:"well"}
d1.update(d3)
print(d1)

#tuple
t = (10,20,30,40,50)
print(t)
print(type(t))
l = len(t)
for i in range(l):
    print(i,t[i])
for i in t:
    print(i)
v = (1,2,3,True,False,None)
print(t+v)
h = (t,v)
print(h)
c =(1,2,3)*3
print(c)
print(c[2:4])
l=(10,20,30)
t = tuple(l)
j = hash(l)
print(t)
print(j)

#tuple methods
print(min(l))
print(max(l))
print(l.count(10))
print(l.index(20))
print(sum(l))

#sets
s = {"a","b","c","d","e"}
print(s)
s.add("f")
print(s)
f={1,2,3,4}
g = s.union(f)
print(g)
a1 = set()
a2 = set()
for i in range(5):
    a1.add(i)
for i in range(3,5):
    a2.add(i)
a3 = a1.intersection(a2)
print(a3)
a4 = a1.difference(a2)
print(a4)

def my_fun(name):
    print("hello",name)
my_fun("python")

def func(a=0,b=0):
    print("Add",a+b)
func(3)

def fun(*city):
    print("City is ",city)
fun("a","b","c")

def fun(city1,city2 ,city3):
    print("city",city1)
fun("a","b","c")

def func(**city):
    print("city",city[k])
def func(k="a",j="b",l="c"):
    print(k)
func()

#file operation
f= open("new1.txt","w")
f.write("this is first line")
f.write("\nabc")
f.close()

f= open("new1.txt","r")
print(f.read())
for each in f:
    print(each)
f.close()
with open("new1.txt") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
