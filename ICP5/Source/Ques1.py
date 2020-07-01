import pandas as pd
import matplotlib.pyplot as plt

#Set up the output screen
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = [10, 6]

#Read data
train1 = pd.read_csv('./train.csv')

#Display the scatter plot of GarageArea and SalePrice
plt.scatter(train1.GarageArea, train1.SalePrice, color='red')
plt.xlabel('Garage Area')
plt.ylabel('SalePrice')
plt.show()

#Delete the outlier value of GarageArea
outlier_drop = train1[(train1.GarageArea < 1000) & (train1.GarageArea > 180)]

#Display the scatter plot of GarageArea and SalePrice after deleting
plt.scatter(outlier_drop.GarageArea, outlier_drop.SalePrice, color='blue')
plt.xlabel('Garage Area')
plt.ylabel('SalePrice')
plt.show()