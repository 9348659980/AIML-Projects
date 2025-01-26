import matplotlib.pyplot as plt
labels = ['Apple', 'Banana', 'Mango', 'Date']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Fruit Distribution')
plt.show()