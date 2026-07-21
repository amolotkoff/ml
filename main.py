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
i = 75
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [6, 22, 26, 42, 62, 86, 114, 146]

quadratic = tr.quadratic(x, y)

for _ in range(i):
    e, a, b, c = quadratic()

plt.title("Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x, y)
x_fit = np.linspace(-10, 10, 10)
y_fit = a * (x_fit**2) + b*x_fit + c
plt.plot(x_fit, y_fit, marker= 'o')
plt.show()




