import numpy as np

#ques1
arr = np.random.rand(5)
print(arr)

arr = np.empty([4,2])
print(arr)
arr = np.full([4,2],3)
print(arr)

arr = np.zeros([3,5],int)
print(arr)

arr = np.ones([4,3,2])
print(arr)

#ques2
arr = np.arange(2,11)
matrix = arr.reshape(3,3)
print(matrix)

#ques3
arr = np.zeros(10,int)
arr[5] = 11
print(arr)

#ques4
arr = np.array([1,2,3,4,5,6])
print(arr[::-1])

#ques5
arr = np.array([1,2,3,4])
print(arr.astype(float))