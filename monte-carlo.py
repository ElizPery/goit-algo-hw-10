import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Define the function and the integration limit
def f(x):
    return x ** 2

a = 0  # Lower limit
b = 2  # Upper limit

# Create a value range for x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Create a graph
fig, ax = plt.subplots()

# Drawing a function
ax.plot(x, y, 'r', linewidth=2)

# Fill the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Gragh Setup
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Add integration limits and gragh name
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Integration graph f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Calculate integral by Monte Carlo method
def monte_carlo(a, b, num_samples):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)

    # Number of dots under curve
    under_curve = np.sum(y_random < f(x_random))

    # Area under curve
    area_under_curve = (b - a) * f(b) * (under_curve / num_samples)

    # Check by quad
    result, error = spi.quad(f, a, b)

    return area_under_curve, result, error


for num in [100, 1000, 10000]:
    area_under_curve, result, error = monte_carlo(a, b, num)
    print(f"Area calculated by Monte-Carlo method: {area_under_curve}; by quad function: {result} with possible error {error}")