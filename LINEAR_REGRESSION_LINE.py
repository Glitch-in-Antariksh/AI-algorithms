import matplotlib.pyplot as plt
# -------- INPUT --------
x = list(map(float, input("Enter x values (space separated): ").split()))
y = list(map(float, input("Enter y values (space separated): ").split()))
n = len(x)
if n != len(y):
    raise ValueError("x and y must have the same number of elements")
# -------- MEANS --------
x_mean = sum(x) / n
y_mean = sum(y) / n
# -------- TABLE CALCULATION --------
dx = []
dy = []
dx_dy = []
dx2 = []

for i in range(n):
    dx_val = x[i] - x_mean
    dy_val = y[i] - y_mean

    dx.append(dx_val)
    dy.append(dy_val)
    dx_dy.append(dx_val * dy_val)
    dx2.append(dx_val ** 2)

# -------- LEAST SQUARES COEFFICIENTS --------
a = sum(dx_dy) / sum(dx2)
b = y_mean - a * x_mean
# -------- DISPLAY TABLE --------
print("\nLeast Squares Table:")
print("x\t y\t x-x̄\t y-ȳ\t (x-x̄)(y-ȳ)\t (x-x̄)²")

for i in range(n):
    print(f"{x[i]:.2f}\t {y[i]:.2f}\t {dx[i]:.2f}\t {dy[i]:.2f}\t "
          f"{dx_dy[i]:.2f}\t\t {dx2[i]:.2f}")

# -------- RESULTS --------
print("\nResults:")
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"Best fit line: y = {a:.4f}x + {b:.4f}")

# -------- PLOTTING --------
y_fit = [a * xi + b for xi in x]

plt.scatter(x, y, label="Data Points")
plt.plot(x, y_fit, label="Best Fit Line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
