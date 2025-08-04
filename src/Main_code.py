# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 15:43:16 2025

@author: illes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import the dataset
data = pd.read_csv(r"C:\Users\illes\OneDrive\Pulpit\Python\Pliki\airlines_flights_data.csv")

data

#cleaning the dataset

data = data.drop(columns=["index"])

print(data)
#Get information aboutut dataset
data.info()
#Get Statistical summary about the dataset
data.describe()

#Show lines where duration is grater then 45h
data[data["duration"]>45.0000]

data.isnull().sum()

#Graph no 1: What are the airlines in the dataset,accompanied by their frequencies?

data.head()
#Check how many Airlines are in the database
len(data["airline"].unique())
#Show the names of the Airlines in the database
data["airline"].unique()
#Show all the Airlines with their frequencies
data['airline'].value_counts()
#Show all the Airlines with their Number of Flights in Bar Graph\
# Create the bar chart
data['airline'].value_counts(ascending=True).plot.barh(color= ['#57A0D2', '#95C8D8'])
# Add title and axis labels with larger font sizes
plt.title('Total flights per Airline', fontsize=16)
plt.xlabel('Airlines', fontsize=14)
plt.ylabel('Number of flights', fontsize=14)
# Rotate x-axis labels and adjust font size
plt.xticks(rotation=45, fontsize=12) 
plt.yticks(fontsize=12)               
# Show the plot
plt.tight_layout()  # Adjust layout to prevent text cutoff
plt.show()


#Graph no 2: Show Bar Graphs representing the Departure Time & Arrival Time

#Showing the Departure and Arrival Time for the flights
data['departure_time'].value_counts()
data['arrival_time'].value_counts()


#Showing the Departure Time for the flights witht their counts
plt.figure(figsize =(16,6))
plt.subplot(1,2,1)
#To deifine x and y for the graph
x = data['departure_time'].value_counts().index
y = data['departure_time'].value_counts().values
plt.bar(x,y, color='#008ECC')
plt.title('Number of flights per Departure Time', fontsize=14)
plt.xlabel('Departure Time', fontsize=12)
plt.ylabel('Departure Frequency', fontsize=12)
# Improve layout
plt.tight_layout()
plt.show()


#Showing the Arrival Time for the flights witht their counts
plt.figure(figsize =(16,6))
plt.subplot(1,2,2)
#To deifine a and b for the graph
a = data['arrival_time'].value_counts().index
b = data['arrival_time'].value_counts().values
plt.bar(a,b, color='#009999')
plt.title('Number of flights per Arrival Time', fontsize=14)
plt.xlabel('Arrival Time', fontsize=12)
plt.ylabel('Arrival Frequency', fontsize=12)
# Improve layout
plt.tight_layout()
plt.show()

#Graph no 3: Show Bar Graphs representing the Source City & Destination City
data.head()

#Showing the source city and destination city of the flights
data['source_city'].value_counts()
data['destination_city'].value_counts()
#Showing the source city of the flights with their counts
plt.figure(figsize= (16,6))
plt.subplot(1,2,1)
#To deifine x and y for the graph
x = data['source_city'].value_counts().index
y = data['source_city'].value_counts().values
plt.bar(x,y, color='#006699')
plt.title('Number of flights per Source City', fontsize=14)
plt.xlabel('Cities', fontsize=12)
plt.ylabel('Number of flights', fontsize=12)
# Improve layout
plt.tight_layout()
plt.show()

#Showing the destination city of the flights with their counts
plt.figure(figsize= (16,6))
plt.subplot(1,2,2)
#To deifine x and y for the graph
x = data['destination_city'].value_counts().index
y = data['destination_city'].value_counts().values
plt.bar(x,y, color='#0080FE')
plt.title('Destination Cities with number of flights', fontsize=14)
plt.xlabel('Cities', fontsize=12)
plt.ylabel('Number of flights', fontsize=12)
# Improve layout
plt.tight_layout()
plt.show()

#Graph no 4: Does price varies with airlines?
data.head()
#Grouping the airlines and checking their mean price
data.groupby('airline')['price'].mean()
#Presenting a Categorical Plot showing the Mean Ticket Price for each Airline
e = sns.catplot(
    x ='airline', 
    y= 'price', 
    kind='bar', 
    palette='pastel', 
    data=data, 
    hue = 'class')
e.set_axis_labels("Airline company", "Price")  
e.fig.suptitle("Avergae Ticket Price per Airline company", fontsize=16)
plt.show()


#Graph no 5: Does ticket price change based on the departure time and arrival time? 
data.groupby('departure_time')['price'].mean()
data.groupby('arrival_time')['price'].mean()

plt.figure(figsize= (22,6))
sns.catplot(
    x ='departure_time', 
    y= 'price', 
    kind='bar', 
    data=data, 
    color='#0080FE')
plt.title('Average Price per Departure Time', fontsize=14)
plt.xlabel('Departure Time', fontsize=12)
plt.ylabel('Average price', fontsize=12)
plt.tight_layout()
plt.show()




f=sns.relplot( 
    x ='arrival_time', 
    y='price', 
    data=data, 
    col= 'departure_time' , 
    kind = 'line',
    color='#33ccff')
f.set_axis_labels("Arrival time", "Price")  
f.fig.suptitle("Ticket Price per Arrival Time", fontsize=16)
f.fig.subplots_adjust(top=0.85)
plt.show()

#Graph no 6: How the price changes with change in Source and Destination?

g= sns.relplot( 
    x ='departure_time', 
    y='price', 
    data=data, 
    col= 'source_city', 
    kind = 'line',
    color='#6699ff')
g.set_axis_labels("Departure time", "Price")  
g.fig.suptitle("Ticket Price per Depture Time", fontsize=16)
g.fig.subplots_adjust(top=0.85)
plt.show()


#Graph no 7: How is the price affected when tickets are bought in just 1 or 2 days before departure? 

data['days_left'].nunique()
data['days_left'].unique()

#Checking the Mean Ticket Price for diffrent days left

data.groupby('days_left')['price'].mean()

f= sns.relplot(
    x ='days_left',
    y = 'price',
    data=data,
    kind = 'line')
f.set_axis_labels("Days Left Before Departure", "Price")  
f.fig.suptitle("Average Ticket Price by Days Remaining Until Departure", fontsize=16)
f.fig.subplots_adjust(top=0.85)
plt.show()


#Graph no 8: How does the ticket price vary between Economy and Bussines Class?
data['class'].unique() 
x = data[data['class'] =='Economy']
x
x.price.mean()
y = data[data['class'] =='Business']
y
y.price.mean()

#Graph no 9: What will be the Average Price of Vistara arline for a flight from Delhi to Hyderabad in Business Class?

x = data[(data['airline']=='Vistara') & (data['source_city'] == 'Delhi') & (data['destination_city']=='Hyderabad')& (data['class']=='Business')]                                                  
x
x['price'].mean()

#Graph 10: Crate pie chart to show the share of flights by source city
# Count the quantity of flights per source city
city_counts = data['source_city'].value_counts()
colors = sns.color_palette("pastel")[0:len(city_counts)]
# Create Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(
        city_counts, 
        labels=city_counts.index, 
        autopct='%1.1f%%', 
        startangle=140,
        colors=colors)
plt.title('Share of Flights by Source City', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()