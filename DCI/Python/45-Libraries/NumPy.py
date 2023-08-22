import numpy as np

my_array = np.array([10, 12, 14, 16, 20, 25], dtype=np.int64)


print(my_array)
print(my_array.dtype)
print(my_array.dtype.itemsize)

print('----------------------------------')
my_array2 = np.array(["red", "green", "orange"])

print(my_array2)
print(my_array2.dtype)
print(my_array2.dtype.itemsize)

print('----------------------------------')
my_array3 = np.array(["1990-10-04", "1989-05-06", "1990-01-01"], dtype='M')

print(my_array3)
print(my_array3.dtype)
print(my_array3.dtype.itemsize)

print('----------------------------------')
my_array4 = my_array3.astype('U')
print(my_array4)
print(my_array4.dtype)
print(my_array4.dtype.itemsize)

print('----------------------------------')
print(type(my_array3))

print('----------------------------------')
row1 = [10, 12, 13]
row2 = [45, 32, 16]
row3 = [11, 33, 45]

nums_2d = np.array([row1, row2, row2])

extended_arr = np.append(nums_2d, [[1, 2, 3]], axis=0)
print(extended_arr)

extended_arr = np.append(nums_2d, [[1], [2], [3]], axis=1)
print(extended_arr)

row_1_2 = [1, 2, 3]
row1 = nums_2d[0:1, :]
row2_3 = nums_2d[1:, :]

new_arr = np.array([row1, row_1_2, row2_3])
print(new_arr)


