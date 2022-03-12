import numpy as np

# task1
data1 = np.random.randn(10,10)
a = data1.min()
b = data1.max()
print(a,b)

# task2
data2 = np.random.randn(5,6)
print(data2)
print(data2.mean())

# task3
data3 = np.random.randn(10)
data3.sort()
print(data3)

# task4
data4 = np.random.randn(10)
print(data4)
data4[data4.argmax()] = 0
print(data4)
