import matplotlib.pyplot as plt
ages = [18, 20, 21, 22, 22, 23, 24, 25, 25, 26, 27, 28, 30, 31, 32, 35]
plt.hist(ages, bins=5, edgecolor="blue")

plt.xlabel("ages")
plt.ylabel("ages distribution")
plt.title("distribution of ages")
plt.show()