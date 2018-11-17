"""
Chapter 2 Problem #4: Visualizing Your Expenses

For this challenge, you'll write a program that creates a bar chart for easy 
comparison of weekly expenditures. The program should first ask for the number
of categories for the expenditures and the weekly total expenditure in each
category, and then it should create the bar chart showing these expenditures.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
import matplotlib.pyplot as plt

def create_bar_chart(data,labels):
    # Number of bars
    num_bars = len(data)
    # This list is the point on the y-axis where each bar is centered.
    # Here it will be [1,2,3...]
    
    positions = range(1, num_bars+1)
    
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Expenditure')
    plt.ylabel('Category')
    plt.title('Weekly Expenditures')
    # Turns on the grid which may assist in visual estimation
    plt.grid()
    plt.show()
    
if __name__ == '__main__':
    num_cat = int(input('Enter the number of categories: '))
    
    categories = []
    expends = []
    
    for i in range(num_cat):
        categories.append(input('Enter category: '))
        expends.append(input('Expenditure: '))
    
    create_bar_chart(expends,categories)