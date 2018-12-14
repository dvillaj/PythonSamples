import numpy as np

from time import clock

my_arr = np.arange(1000000)
my_list = list(range(1000000))

start = clock()
#for _ in range(10): my_arr2 = my_arr * 2
#print("Time ", clock() - start)

#start = clock()
#for _ in range(10): my_list2 = [x * 2 for x in my_list]

print("Time ", clock() - start)

data = np.random.randn(2, 3)
print(data)
print(data * 10)
print(data + 10)
print(data + data)

print(data.shape)
print(data.dtype)