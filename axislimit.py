import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,30,50,70,90]
plt.plot(x,y)
plt.title("Sales Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.xlim(0,10)
plt.ylim(0,100)
plt.show()