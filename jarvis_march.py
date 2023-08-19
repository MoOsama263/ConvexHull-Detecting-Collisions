import random
import matplotlib.pyplot as plt
from typing import List, Set, Tuple

def jarvis_march(X: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    n = len(X)
    l = [min(X)]
    hull_points = [l[0]]
    while True:
        v = l[-1]
        rightmost_idx = 0
        for i in range(n):
            if X[i] == v:
                continue
            cr = cross(v, X[i], X[rightmost_idx])
            if cr < 0 or (cr == 0 and abs(X[i][0] - v[0]) > abs(X[rightmost_idx][0] - v[0])):
                rightmost_idx = i
        if X[rightmost_idx] == hull_points[0]:
            break
        l.append(X[rightmost_idx])
        hull_points.append(X[rightmost_idx])

    return hull_points

# Generate random points
points = []
for i in range(30):
    points.append((random.randint(1, 20), random.randint(1, 20)))

# Plot the points
plt.scatter([p[0] for p in points], [p[1] for p in points], s=10)
plt.pause(1)

# Compute the convex hull using Jarvis march
hull = jarvis_march(points)

# Plot all the segments
for i in range(len(hull)):
    j = (i + 1) % len(hull)
    plt.plot([hull[i][0], hull[j][0]], [hull[i][1], hull[j][1]], '-r', linewidth=1)
    plt.pause(0.01)

for i in range(len(points)):
    if points[i] not in hull:
        closest_hull_point = min(hull, key=lambda p: (p[0]-points[i][0])**2 + (p[1]-points[i][1])**2)
        plt.plot([points[i][0], closest_hull_point[0]], [points[i][1], closest_hull_point[1]], '-g', linewidth=0.5)
        plt.pause(0.01)

# Wait for user to close the plot window
while plt.get_fignums():
    if plt.waitforbuttonpress(0.1):
        plt.close()
        break

plt.show()
