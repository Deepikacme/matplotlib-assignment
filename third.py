import matplotlib.pyplot as plt
x=["jan,feb,mar,apr,may,jun,jul,aug,"]
y=["$100,$200,$300,$400,$500,$600,$700,$800"]
plt.plot("months,sales",linestyle="--",marker="o",color="g")
plt.title("Monthly Sales")
plt.xlabel("Month") 
plt.ylabel("Sales") 
plt.show()