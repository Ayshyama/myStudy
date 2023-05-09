# 09.05.2023
# Task - Matrix mean

def mean(numbers):
    output = []
    for row in numbers:
        row_mean = sum(row) / len(row)
        output.append(row_mean)
    return output


numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
print(mean(numbers))