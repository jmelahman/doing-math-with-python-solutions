"""
Chapter 2 Problem #1: How Does the Temperature Vary During the Day

Using a city of your choice, find the temperature at different points of the
day. Use the data to create two lists in your program and to create a graph
with the time of the day on the x-axis and the corresponding temperature on the
y-axis. The graph should tell you how the temperature varies with the time of
day. Try a different city and see how the two cities compare by plotting both
lines on the same graph.

The time of day may be indicated by strings such as '10:11 AM' or '09:21 PM'

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
import matplotlib.pyplot as plt


def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Time of Day')

    plt.ylabel('Temperature')
    plt.title('Temperature During the Day')


if __name__ == '__main__':
    time = [0.0, 4.0, 8.0, 12.0, 16.0]
    sf_temp = [48.0, 46.0, 44.0, 55.0, 59.0]
    cin_temp = [38.0, 32.0, 40.0, 42.0, 45.0]

    draw_graph(time, sf_temp)
    draw_graph(time, cin_temp)
    plt.show()
