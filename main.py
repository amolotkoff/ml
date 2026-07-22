from matplotlib.pyplot import legend

import train as tr
import matplotlib.pyplot as plt
import numpy as np

#
# a = 0
# e = 0
# b = 0
# i = 3
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [2, 4, 6, 8, 10, 12, 14, 16]
#
# linear = tr.linear(x, y)
#
# for _ in range(i):
#     e, a, b = linear()
#
# plt.title("Regression")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.scatter(x, y)
# plt.plot([0, 8], [b, a * 8 + b], marker= 'o')
# plt.show()
#

e = 0
a = 0
b = 0
c = 0
i = 50
x = [-9.8, -8.5, -7.2, -6.1, -5.4, -4.3, -3.2, -2.1, -1.5, -0.8, 0.0, 0.7, 1.4, 2.3, 3.1, 4.2, 5.0, 6.3, 7.1, 8.4]
y = [165.2, 130.4, 98.7, 72.3, 55.8, 38.1, 24.9, 14.2, 9.1, 5.8, 3.2, 4.1, 8.7, 16.9, 27.8, 44.3, 59.2, 86.7, 106.3, 143.8]

quadratic = tr.quadratic(x, y)

for _ in range(i):
    e, a, b, c = quadratic()

plt.title("Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x, y)
x_fit = np.linspace(-10, 10, 100)
y_fit = a * (x_fit**2) + b*x_fit + c
plt.plot(x_fit, y_fit)
plt.show()




