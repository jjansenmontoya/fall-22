import matplotlib.pyplot as plt

x = [1, 4, 10]
y = [5.8, 12800, 12800000]
c = [2, 100, 5000]

plt.scatter(x, y, 'o')
plt.errorbar(x, y, yerr = c, fmt = 'o')

plt.show()