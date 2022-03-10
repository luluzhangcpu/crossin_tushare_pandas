# task1 导入numpy
import numpy as np

# task2 查询numpy的版本及配置
print(np.__version__)
np.show_config()

# task4 构建1个数组；并计算它的所占字节数；
array1 = np.zeros(10)
a = array1.size * array1.itemsize
print('共占 %d Bytes' % a)

# task5 查询 add 函数
np.info(np.add)
