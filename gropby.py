import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({
    "Department":["HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],    
    "Salary":[50000, 60000, 55000, 70000, 52000, 58000, 75000]
      })
summary=df.groupby('Department')['Salary'].mean()
plt.bar(summary.index, summary.values)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()