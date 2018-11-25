"""
Chapter 3 Problem #1: Better Correlation Coefficient Finding Program

The find_coor_x_y() function we wrote earlier to find the correlation 
coefficient between two sets of numbers assumes that the two sets of numbers 
the same length. Improve the function so that it first checks the length of the
lists. If they're equal, only then should the function proceed with the 
remaining calculations; otherwise, it should print an error message that the
correlation can't be found.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""

def find_corr_x_y(x,y):
    n = len(x)
    
    # Find the sum of the products
    prod = []
    
    for xi,yi in zip(x,y):
        prod.append(xi*yi)
    
    sum_prod_x_y = sum(prod)
    
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2
    
    x_square = []
    y_square = []
    
    for xi in x:
        x_square.append(xi**2)
    
    for yi in y:
        y_square.append(yi**2)
    # Find the sums
    x_square_sum = sum(x_square)
    y_square_sum = sum(y_square)
    
    # Use formula to calculate correlation
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    
    denominator = (denominator_term1*denominator_term2)**0.5
    
    correlation = numerator/denominator
    return correlation

if __name__ == '__main__':
    hs_grades = [90,92,95,96]
    college_scores = [85,87,86]
    
    if len(hs_grades) == len(college_scores):
        find_corr_x_y(hs_grades,college_scores)
    else:
        print('Correlation cannot be found. List size mismatch.')