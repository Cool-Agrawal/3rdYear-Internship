a = 20
b=15
res = a+b
print(res)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
res = 2+5*10-20
print(res)
print(2**6)
res %= 3
print(res)
if a is not b:
    print(a)
str = "Python"
if 'p' not in str:
    print("yes")
print(bin(a))
print(bin(b))
print(a & b)
print(bin(a & b))
n = int(input("Enter a no\n"))
if n%2 == 0:
    print("Number is even")
else:
    print("Number is odd")

per = int(input("Percentage:"))
if per>90:
    print("Grade A")
elif per>70:
    print("Grade B")
elif per>50:
    print("Grade C")
else:
    print("Fail")
a,b = map(int,input("Enter two numbers").split())
value = int(input("Enter 1 for add ,2 for sub,3 for multiply,4 for divide"))
if value == 1:
    print(a+b)
elif value == 2:
    print(a-b)
elif value == 3:
    print(a*b)
elif value == 4:
    print(a/b)
else:
    print("Other")
print("a") if a%2 == 0 else print(b)
for i in range(1,20,2):
    print(i)
a = int(input("Enter a no"))
for i in range(1,11):
    if i == 5:
        continue
    print(a,"x",i,"=",a*i)
for i in range(1,5):
    for j in range(1,i+1):
        print(j ,end="")
    print("\n")
k=0
while k<10:
      print(k)
      k+=2
while True:
      n = int(input("enter n"))
      if n==0:
          break
      print(n)
g="Hello"
print(ascii(g))
k =[1,2,3,4,5,"java"]
k.reverse()
print(k)
l =[1,2,3]
l.append({4,5})
l.extend({6,7})
print(l)
