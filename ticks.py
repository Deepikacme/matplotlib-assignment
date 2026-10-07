import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May"]
sales = [20, 40, 60, 80, 100]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.yticks([0, 20, 40, 60, 80, 100])
plt.show()