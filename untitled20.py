import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [2, 5, 6]
plt.plot(x1, y1, label = "Line 1")

x2 = [1, 2, 3]
y2 = [2, 1, 3]
plt.plot(x2, y2, label = "Line 2")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two Lines on the Same Graph')

plt.legend()
plt.show()