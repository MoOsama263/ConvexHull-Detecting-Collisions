import math
import random
import matplotlib.pyplot as plt
from typing import List, Tuple

def graham_scan(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    def polar_angle(p: Tuple[float, float], q: Tuple[float, float]) -> float:
        x_diff = q[0] - p[0]
        y_diff = q[1] - p[1]
        return math.atan2(y_diff, x_diff)

    def is_left_turn(p: Tuple[float, float], q: Tuple[float, float], r: Tuple[float, float]) -> bool:
        return ((q[0] - p[0]) * (r[1] - p[1])) > ((r[0] - p[0]) * (q[1] - p[1]))

    # Initialize the figure and plot the initial set of points
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter([p[0] for p in points], [p[1] for p in points], color='blue')
    plt.pause(0.1)

    # Find the bottom-most point
    bottom = min(points, key=lambda p: p[1])
    ax.scatter(bottom[0], bottom[1], color='green')
    plt.pause(0.1)

    # Sort the points by polar angle with respect to the bottom-most point
    sorted_points = sorted(points, key=lambda p: polar_angle(bottom, p))
    ax.plot([bottom[0], sorted_points[0][0]], [bottom[1], sorted_points[0][1]], color='red')
    plt.pause(0.1)

    # Initialize the stack
    stack = [sorted_points[0], sorted_points[1]]
    ax.scatter(stack[0][0], stack[0][1], color='green')
    ax.scatter(stack[1][0], stack[1][1], color='green')
    plt.pause(0.1)

    # Perform the Graham scan
    for i in range(2, len(sorted_points)):
        while len(stack) > 1 and not is_left_turn(stack[-2], stack[-1], sorted_points[i]):
            stack.pop()
            ax.plot([stack[-1][0], sorted_points[i][0]], [stack[-1][1], sorted_points[i][1]], color='red')
            plt.pause(0.1)
        stack.append(sorted_points[i])
        ax.scatter(sorted_points[i][0], sorted_points[i][1], color='blue')
        ax.plot([stack[-2][0], stack[-1][0]], [stack[-2][1], stack[-1][1]], color='green')
        ax.plot([stack[-1][0], sorted_points[i][0]], [stack[-1][1], sorted_points[i][1]], color='red')
        plt.pause(0.1)

    # Plot the final convex hull
    ax.plot([p[0] for p in stack] + [stack[0][0]], [p[1] for p in stack] + [stack[0][1]], color='green')
    plt.pause(0.1)

    plt.show()

    return stack

# Generate random points
points = []
for i in range(30):
    points.append((random.randint(1, 20), random.randint(1, 20)))

# Compute the convex hull using Graham scan
hull = graham_scan(points)

# Plot all the segments
for i in range(len(hull)):
    j = (i + 1) % len(hull)
    plt.plot([hull[i][0], hull[j][0]], [hull[i][1], hull[j][1]], '-r', linewidth=1)
    plt.pause(0.1)

for i in range(len(points)):
    if points[i] not in hull:
        closest_hull_point = min(hull, key=lambda p: (p[0]-points[i][0])**2 + (p[1]-points[i][1])**2)
        plt.plot([points[i][0], closest_hull_point[0]], [points[i][1], closest_hull_point[1]], '-g', linewidth=0.5)
        plt.pause(0.1)

# Wait for user to close the plot window
while plt.get_fignums():
    if plt.waitforbuttonpress(0.1):
        plt.close()
        break

plt.show()