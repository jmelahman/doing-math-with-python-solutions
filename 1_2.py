"""
Chapter 1 Problem #2: Enahnced multiplcation table generator

Our multiplication table generator is cool, but it prints only the first 10 multiples. Enhance the generator so that the user can specify both the number and up to which multiple. For example, I should be able to input that I want to see a table listing the first 15 multiples of 9.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
def enhanced_multi_table(a, end_mult):
    for i in range(1,int(end_mult)+1):
        print('{0} x {1} = {2}'.format(a,i,a*i))
    return()

if __name__ == '__main__':
    a = input('Enter a number: ')
    b = input('Enter the last multiple: ')
    enhanced_multi_table(float(a),b)