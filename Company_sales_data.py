#Company_sales_data.Assignment 
####### 1. Read Total profit of all months and show it using a line plot

import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data.csv')
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
################### 2. Get total profit of all months and show line plot with the following Style properties
#Generated line plot must include following Style properties: –
#Line Style dotted and Line-color should be red
#Show legend at the lower right location.
#X label name = Month Number
#Y label name = Sold units number
#Add a circle marker.
#Line marker color as read
#Line width should be 3

import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data.csv')
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
######## 3. Read all product sales data and show it  using a multiline plot
# #Display the number of units sold per month for each product using multiline plots.
# (i.e., Separate Plotline for each product ).

import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data.csv')
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()
##########  4. Read toothpaste sales data of each month and show it using a scatter plot
#Also, add a grid in the plot. gridline style should “–“.
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data.csv')
monthList  = df ['month_number'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()
###############  5. Read face cream and facewash product sales data and show it using the bar chart
#The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data.csv')
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()
###########  6. Read sales data of bathing soap of all months and show it using a bar chart.#####################
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data.csv')
monthList  = df ['month_number'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title(' Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('bathingsoap sales data')
plt.savefig(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data_of_bathingsoap.png', dpi=150)
plt.show()
###############  7. Calculate total sale data for last year for each product and show it using a Pie chart################
import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data.csv')
monthList  = df ['month_number'].tolist()

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(), 
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.savefig(r'E:\Croma campus traning $developer (p) ltd\Python\company_sales_data_of_Toothpaste.png', dpi=150)
plt.show()
############
####EXTRA DATA #####

###question 01
##Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
##Sample data:
##Programming languages: Java, Python, PHP, JavaScript, C#, C++
###Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


######################################
### Question 02
##Write a Python programming to display a bar chart of the popularity of programming Languages.
##Sample data:
##Programming languages: Java, Python, PHP, JavaScript, C#, C++
##Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
######################
### Question 03
###Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016.
##Sample Financial data (fdata.csv):
##Date,Open,High,Low,Close
##10-03-16,774.25,776.065002,769.5,772.559998
##10-04-16,776.030029,778.710022,772.890015,776.429993
##10-05-16,779.309998,782.070007,775.650024,776.469971
##10-06-16,779,780.47998,775.539978,776.859985
##10-07-16,779.659973,779.659973,770.75,775.080017 

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'E:\Croma campus traning $developer (p) ltd\Python\fdata.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()
#######################

