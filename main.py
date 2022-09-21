import matplotlib.pyplot as plt
import numpy as np

f = lambda x, y: y / np.tan(x) + 2 * x * np.sin(x)

x = 1
y = 1
tau = 0.001

b = np.array(([0, 0, 0],
              [1/3, 0, 0],
              [-1/3, 0, 0],
              [1, -1, 1]))

l = np.array([1/8, 3/8, 3/8, 1/8])
a = np.array([0, 1/3, 2/3, 1])

while x <= 2:
    plt.plot(x, y, marker='.', color='black')
    plt.plot(x, f(x, y), marker='.', color='blue')

    i = 0
    k = np.zeros(4)
    while i <= 3:
        k[i] = f(x + a[i] + tau, y + b[i, 0] * tau * k[0] +  b[i, 1] * tau * k[1] +  b[i, 2] * tau * k[2] )
        i += 1
    y += tau * np.inner(k, l)
    x += tau

print("dx = ", tau)
print("y(2) = ", y)

plt.grid()
plt.show()
