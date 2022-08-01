import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x, y, label = "stars", color = "purple",
            marker = "*", s = 30)

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title("Plot")
plt.legend()

plt.show()