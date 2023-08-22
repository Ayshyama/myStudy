import numpy as np
import timeit

list_nums = [i for i in range(100000)]
numpy_nums = np.array(list_nums)


def multiply_list(nums):
    return [i*2 for i in nums]


def multiply_numpy(nums):
    return nums * 2


time_list = timeit.timeit(lambda: multiply_list(list_nums), number=100)
time_numpy = timeit.timeit(lambda: multiply_numpy(numpy_nums), number=100)


print(f"List time: {time_list:.4f} seconds")
print(f"NumPy time: {time_numpy:.4f} seconds")
speed = time_list/time_numpy
print(f"NumPy is faster for: {speed:.4f} times")

list_nums_2d = [[i+j for i in range(10000)] for j in range(10000)]
numpy_nums_2d = np.array(list_nums_2d)


def multiply_2dlist(nums):
    return [[i*2 for i in row] for row in nums]


def multiply_2dnumpy(nums):
    return nums * 2


list_time_2d = timeit.timeit(lambda: multiply_2dlist(list_nums_2d), number=100)
numpy_time_2d = timeit.timeit(lambda: multiply_2dnumpy(numpy_nums_2d), number=100)


print(f"2D List time: {list_time_2d:.4f} seconds")
print(f"2D NumPy time: {numpy_time_2d:.4f} seconds")
speed_2d = list_time_2d/numpy_time_2d
print(f"NumPy is faster for: {speed_2d:.4f} times")
