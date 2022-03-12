import numpy as np

# task1
# Given a 1D array, negate all elements which are between 3 and 8, in place.
# (给定一个一维数组，将元素值在3至8之间的元素置为其原本的相反数)
# 第一种做法
data1 = np.arange(32).reshape((4,8))
for i in range(4):
    for j in range(8):
        if data1[i,j] >= 3 and data1[i,j] <= 8:
            data1[i,j] = - data1[i,j]
print(data1)

# 第二种做法
a = data1 >= 3
b = data1 <= 8
print(data1[a & b])
data1[a & b] = data1[a & b] * (-1)
print(data1)

# task2 
# How to swap two rows of an array? (如何交换一个数组的两行？)
data1[[2,3]] = data1[[3,2]]
print(data1)
