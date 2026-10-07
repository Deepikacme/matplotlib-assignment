import matplotlib.pyplot as plt

months=["Jan","Feb","Mar","Apr"]
sales=[100,150,120,180]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig(
    "sales_chart.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
