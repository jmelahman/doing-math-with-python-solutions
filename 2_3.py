"""
Chapter 2 Problem #3: Enhanced Projectile Trajectory Comparison

Your challenge here is to enhance the trajectory comparison program in a few
ways. First, your program should print the time of flight, maximum horizontal
distance, and maximum vertical distance traveled for each of the velocity and
angle of projection values, supplied by the user. For example, here's how the
program should ask the user for inputs:

How many trajectories? 3
Enter the initial velocity for trajectory 1 (m/s): 45
Enter the angle of projection for trajectory 1 (degrees): 45
Enter the initial velocity for trajectory 1 (m/s): 60
Enter the angle of projection for trajectory 1 (degrees): 45
Enter the initial velocity for trajectory 1 (m/s): 45
Enter the angle of projection for trajectory 1 (degrees): 90

Your program should also ensure the erroneous input is properly handled using a
try. . . except block, just as in the original program.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
import matplotlib.pyplot as plt
import math


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')


def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval

    return numbers


def draw_trajectory(u, theta):

    theta = math.radians(theta)
    g = 9.81

    # Time of flight
    t_flight = 2 * u * math.sin(theta) / g
    # Fine time intervals
    intervals = frange(0, t_flight, 0.001)

    # lList of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)

    print('Time of flight: {0}'.format(t_flight))
    print('Max horizontal distance: {0}'.format(max(x)))
    print('Max vertical distance: {0}'.format(max(y)))

    draw_graph(x, y)


if __name__ == '__main__':
    num_traj = int(input('How many trajectories? '))
    for i in range(num_traj):
        try:
            u = float(input('Enter the initial veolcity (m/s): '))
            theta = float(input('Enter the angle of projection (degrees): '))
        except ValueError:
            print('You enter an invalid input')
        else:
            draw_trajectory(u, theta)

    plt.show()
