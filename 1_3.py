"""
Chapter 1 Problem #3: Enhanced Unit Converter

The unit conversion program we wrote in this chapter is limited to conversions
between kilometers and miles. Try extending the program to convert between
units of mass (such as kilograms and pounds) and between units of temperature
(such as Celsius and Fahrenheit).

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')
    print('5. Kilograms to Pounds')
    print('6. Pounds to Kilograms')

def km_mi():
    km = float(input('Enter distance in kilometers: '))
    mi = km / 1.609
    
    print('Distance in miles: {0}'.format(mi))

def mi_km():
    mi = float(input('Enter distance in miles: '))
    km = mi * 1.609
    
    print('Distance in kilometers: {0}'.format(km))

def c_f():
    c = float(input('Enter temperature in Celsius: '))
    f = c * (9 / 5) + 32
    
    print('Temperature in Fahrenheit: {0}'.format(f))

def f_c():
    f = float(input('Enter temperature in Fahrenheit: '))
    c = (f - 32) * (5 /9)
    
    print('Temperature in Celsius: {0}'.format(c))

def kg_lbs():
    kg = float(input('Enter mass in kilograms: '))
    lbs = kg * 2.2046
    
    print('Mass in pounds: {0}'.format(lbs))

def lbs_kg():
    lbs = float(input('Enter mass in pounds: '))
    kg = lbs / 2.2046
    
    print('Mass in kilograms: {0}'.format(kg))

if __name__ == '__main__':
        print_menu()
        
        choice = input('Which conversion would you like to do?: ')
        if choice == '1':
            km_mi()
        if choice == '2':
            mi_km()
        if choice == '3':
            c_f()
        if choice == '4':
            f_c()
        if choice == '5':
            kg_lbs()
        if choice == '6':
            lbs_kg()
