import matplotlib.pyplot as plt

months=["Jan", "Feb", "Mar", "Apr", "May"]
revenue=[10000, 15000, 12000, 18000, 20000]
plt.plot(months, revenue)
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(axis="y")
plt.show()