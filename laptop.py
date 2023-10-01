import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("laptops\mindfactory_done.csv")
data=pd.DataFrame(df)
print(data.iloc[:,1])

name = list(data.iloc[:5,1])
price = list(data.iloc[:5,0])


# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(price,name, color='blue')

# Add title and labels
plt.title('Laptops and their prices')
plt.xlabel('Laptop name')
plt.ylabel('Price')

# Show the bar chart
plt.show()