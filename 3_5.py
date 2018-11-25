"""
Chapter 3 Problem #5: Creating a Grouped Frequency Table

For this challenge, your task is to write a program that creates a grouped 
frequency table from a set of numbers. A grouped frequency table displays the
frequency of data calssified into different classes. For example, let's
consider the scores we discussed in "Creating a Frequency Table" on page 69:
7,8,9,2,10,9,9,9,9,4,5,6,1,5,6,7,8,6,1, and 10.A grouped frequency table would 
display the data as follows:
        Grade        Frequency
        1-6          6
        6-11         14
Your challenge is two write a program to read a list of numbers from a file and
then to print the grouped frequency table making use of the create_classes()
function.        

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))
    
    return numbers

def create_classes(numbers, n):
    low = min(numbers)
    high = max(numbers)
    
    # Width of each class
    width = (high - low)/n
    a = low
    b = low + width
    classes = []
    while a < (high-width):
        classes.append((a, b))
        a = b
        b = a + width
    # The last class may be of a size that is less than width
    classes.append((a, high+1))
    return classes

def assign_freq(numbers,classes):
    freq = [0]*len(classes)
    for n in numbers:
        for i, c in enumerate(classes):
            if n >= c[0] and n < c[1]:
                freq[i] += 1
                break
    return freq

if __name__ == '__main__':
    data = read_data('mydata.txt')
    bins = 3
    classes = create_classes(data, bins)
    freq = assign_freq(data, classes)
    print('Range\t\tFrequency')
    for i,c in enumerate(classes):
        print('{0}\t{1}'.format(c,freq[i]))