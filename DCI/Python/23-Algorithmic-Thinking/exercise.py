import matplotlib.pyplot as plt
import math

X = [1, 2, 3, 4, 5]

# Calculate Euler's number
euler = math.exp(1)
print(euler)

# Calculate the y-values for each function
Y_logN = [math.log(num) for num in X]
Y_N = X
Y_NlogN = [num * math.log(num) for num in X]
Y_N_square = [num**2 for num in X]
Y_N_exp = [euler**num for num in X]


# Define the factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


Y_N_fact = [factorial(num) for num in X]

# Set up the plot
plt.plot(X, Y_logN, label='logN')
plt.plot(X, Y_N, label='N')
plt.plot(X, Y_NlogN, label='NlogN')
plt.plot(X, Y_N_square, label='N_square')
plt.plot(X, Y_N_exp, label='N_exp')
plt.plot(X, Y_N_fact, label='N!')

# Set the x and y-axis labels
plt.xlabel('X')
plt.ylabel('Y')

# Set the axis limits
plt.xlim(1, 4.0)
plt.ylim(None, 50)  # y max - 50

# Add a legend
plt.legend()

# Show the plot
plt.show()

