import numpy as np

# task1
# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
# (创建一个5x5的矩阵，将在主对角线之下一行值赋值为1，2，3，4)

data1 = np.diag(np.arange(1,5),k = -1)
print(data1)

# task2 
# Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) 
# (将一个5x3的矩阵与一个3x2的矩阵相乘)

a = np.random.randn(5,3)
b = np.random.randn(3,2)
c = np.dot(a,b) # 第一种做法
d = a @ b # 第二种做法
print(c)
print(d)
