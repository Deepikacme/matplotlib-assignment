import matplotlib.pyplot as plt
products=["laptop","mobile","tablet","desktop"]
sales=[100,200,300,400]
plt.bar(products,sales,color="g")
plt.title("sales performance")
plt.xlabel("products")
plt.ylabel("sales")
plt.show()