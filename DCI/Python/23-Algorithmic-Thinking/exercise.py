import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import numpy as np

X = [1, 2, 3, 4, 5]

# Calculate Euler's number
euler = np.exp(1)
print(euler)

# Calculate the y-values for each function
Y_logN = [np.log(num) for num in X]
Y_N = X
Y_NlogN = [num * np.log(num) for num in X]
Y_N_square = [num**2 for num in X]
Y_N_exp = [euler**num for num in X]


# Define the factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


Y_N_fact = [factorial(num) for num in X]

# Set up the figure and axes for 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the functions in 3D
ax.plot(X, Y_logN, np.zeros_like(X), label='logN')
ax.plot(X, Y_N, np.zeros_like(X), label='N')
ax.plot(X, Y_NlogN, np.zeros_like(X), label='NlogN')
ax.plot(X, Y_N_square, np.zeros_like(X), label='N^2')
ax.plot(X, Y_N_exp, np.zeros_like(X), label='N^e')
ax.plot(X, Y_N_fact, np.zeros_like(X), label='N!')

# Set the x, y, and z-axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the axis limits
ax.set_xlim(1, 4.0)
ax.set_ylim(-50, None)
ax.set_zlim(0, None)

# Add a legend
ax.legend()

# Show the plot
plt.show()