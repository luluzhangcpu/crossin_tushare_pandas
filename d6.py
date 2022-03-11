import numpy as np

# task1
data1 = np.arange(10)
data1 = data1[::-1]
print(data1)

# task2
data2 = np.zeros((4,4))
data2[0] = 1
data2[-1] = 1
data2[:,0] = 1
data2[:,-1] = 1
print(data2)

# task3
data3 = np.empty((8,8))
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                data3[i,j] = 1
            else:
                data3[i,j] = 0
        else:
            if j % 2 != 0:
                data3[i,j] = 1
            else:
                data3[i,j] = 0
print(data3)

# task4
data4 = np.array([1,2,3,4,5])
data4 = data4.reshape((5,))
data5 = np.zeros((5,4))
for i in range(5):
    data5[i,0] = data4[i]
data5 = data5.reshape((-1,))
print(data5)

# task5
data6 = np.array([1,2,5,34,76,88,56])
a = data6[::2] # 当最后1个数为正数时，即 step > 0，按递增索引去取数；
print(a) # 这里，即step = 2,前面没写 start索引，即，索引为 0；即，取索引为 0，2，4，6的数；
b = data6[::-1] # 这里即倒序，取数，没写 start，则默认，start为最后1个数；
print(b) # 结果为：[56 88 76 34  5  2  1]
c = data6[4::-1] # 先取索引为4处，再按 step = -1，倒序数
print(c) # 结果为：[76 34  5  2  1]
d = data6[5::-2] # 先取索引为5处，再按 step = -2，倒序数
print(d) # 结果为：[88 34  2]
e = data6[::-3] # 这里即倒序，取数，没写 start，则默认，start为最后1个数；再按 step = -3，取数；
print(e) # 结果为：[56 34  1]
