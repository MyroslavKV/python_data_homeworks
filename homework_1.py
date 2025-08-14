import numpy as np

#Завдання 1#
arr = np.arange(10, 20)

sum_arr = arr.sum()
print(sum_arr)

average_arr = arr.mean()
print(average_arr)

max_arr = arr.max()
print(max_arr)

min_arr = arr.min()
print(min_arr)

#Завдання 2#
large_float64 = np.random.rand(1000).astype(np.float64)

sum_large_float64 = large_float64.sum()
print(sum_large_float64)

average_large_float64 = large_float64.mean()
print(average_large_float64)

max_large_float64 = large_float64.max()
print(max_large_float64)

min_large_float64 = large_float64.min()
print(min_large_float64)

#Завдання 3#
arr = np.arange(1, 26).reshape(5, 5)
print(arr)

second_column = arr[:, 1]
print(second_column)

second_row = arr[1, :]
print(second_row)

flattened = arr.flatten()
print(flattened)

#Завдання 4#
large_float64 = np.random.rand(500000).astype(np.float64)

sum_large_float64 = large_float64.sum()
print(sum_large_float64)

average_large_float64 = large_float64.mean()
print(average_large_float64)

max_large_float64 = large_float64.max()
print(max_large_float64)

min_large_float64 = large_float64.min()
print(min_large_float64)