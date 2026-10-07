import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]
customers = [50, 80, 60, 100]

# 1. Create a figure
plt.figure(figsize=(8, 6))

# 2. Line plot
plt.plot(months, sales, label="Sales")

# 3. Bar chart
plt.bar(months, customers, alpha=0.5, label="Customers")

# 4. Horizontal bar chart
plt.barh(months, sales, alpha=0.3)

# 5. Histogram
plt.hist(sales, bins=5, alpha=0.5)

# 6. Scatter plot
plt.scatter(months, sales)

# 7. Pie chart
plt.figure()
plt.pie(sales, labels=months, autopct="%1.1f%%")

# 8. Box plot
plt.figure()
plt.boxplot(sales)

# 9. Fill between
plt.figure()
x = [1, 2, 3, 4]
y = [10, 20, 15, 30]
plt.plot(x, y)
plt.fill_between(x, y)

# 10. Stem plot
plt.figure()
plt.stem(x, y)

# 11. Subplots
fig, ax = plt.subplots()
ax.plot(months, sales)
ax.set_title("Monthly Sales")

# 12. Title and labels
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# 13. Legend
plt.legend()

# 14. Grid
plt.grid()

# 15. X-axis limit
plt.xlim(0, 5)

# 16. Y-axis limit
plt.ylim(0, 200)

# 17. X ticks
plt.xticks(rotation=45)

# 18. Y ticks
plt.yticks([0, 50, 100, 150, 200])

# 19. Annotation
plt.annotate(
    "Highest Sales",
    xy=("Apr", 180)
)

# 20. Adjust layout
plt.tight_layout()

# 21. Save graph
plt.savefig("sales_chart.png", dpi=300, bbox_inches="tight")

# 22. Show graph
plt.show()