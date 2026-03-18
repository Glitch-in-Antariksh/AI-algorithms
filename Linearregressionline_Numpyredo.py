import numpy as np
import matplotlib.pyplot as plt

# -------- INPUT --------
x = np.array(list(map(float, input("Enter x values (space separated): ").split())))
y = np.array(list(map(float, input("Enter y values (space separated): ").split())))

if len(x) != len(y):
    raise ValueError("x and y must have the same number of elements")

# -------- LEAST SQUARES COEFFICIENTS --------
# np.polyfit finds the best-fit line coefficients [a, b] for y = ax + b
a, b = np.polyfit(x, y, 1)

# -------- DISPLAY TABLE --------
dx = x - x.mean()
dy = y - y.mean()

print("\nLeast Squares Table:")
print("x\t y\t x-x̄\t y-ȳ\t (x-x̄)(y-ȳ)\t (x-x̄)²")
for i in range(len(x)):
    print(f"{x[i]:.2f}\t {y[i]:.2f}\t {dx[i]:.2f}\t {dy[i]:.2f}\t "
          f"{(dx[i]*dy[i]):.2f}\t\t {dx[i]**2:.2f}")

# -------- RESULTS --------
print(f"\na = {a:.4f}")
print(f"b = {b:.4f}")
print(f"Best fit line: y = {a:.4f}x + {b:.4f}")

# -------- PLOTTING --------
y_fit = np.polyval([a, b], x)   # evaluates ax + b for each x

plt.scatter(x, y, label="Data Points")
plt.plot(x, y_fit, label="Best Fit Line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()