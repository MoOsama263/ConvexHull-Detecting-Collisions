import random
import matplotlib.pyplot as plt
from typing import List, Tuple

def find_hull_points(points):
    if len(points) <= 3:
        return points

    leftmost = min(points, key=lambda p: p[0])
    rightmost = max(points, key=lambda p: p[0])
    topmost = max(points, key=lambda p: p[1])
    bottommost = min(points, key=lambda p: p[1])

    hull = [leftmost, rightmost, topmost, bottommost]
    points = [p for p in points if p not in hull]

    for p in points:
        if ((p[0] == leftmost[0] or p[0] == rightmost[0]) and p[1] >= bottommost[1] and p[1] <= topmost[1]) or \
                ((p[1] == topmost[1] or p[1] == bottommost[1]) and p[0] >= leftmost[0] and p[0] <= rightmost[0]):
            hull.append(p)

    return hull

def quickhull(X: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    def distance(p, q, r):
        return ((q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]))

    def qhull(points, p, q):
        if not points:
            return []

        max_d = 0
        farthest_point = None
        for point in points:
            d = distance(p, q, point)
            if d > max_d:
                max_d = d
                farthest_point = point

        if not farthest_point:
            return []

        new_points = [point for point in points if distance(p, farthest_point, point) > 0]
        convex_hull = []

        convex_hull.extend(qhull(new_points, p, farthest_point))
        convex_hull.append(farthest_point)
        convex_hull.extend(qhull(new_points, farthest_point, q))

        return convex_hull

    hull_points = find_hull_points(X)
    if len(hull_points) <= 3:
        return hull_points

    convex_hull = []

    for i in range(len(hull_points)):
        p = hull_points[i]
        q = hull_points[(i+1) % len(hull_points)]
        convex_hull.extend(qhull(X, p, q))

    return list(set(convex_hull))

# Generate random points
points = []
for i in range(30):
    points.append((random.randint(1, 20), random.randint(1, 20)))

# Find the extreme points and compute the convex hull
hull_points = find_hull_points(points)
hull = quickhull(hull_points)

# Plot the points and the convex hull of the extreme points
plt.scatter([p[0] for p in points], [p[1] for p in points], s=10)
for i in range(len(hull)):
    j = (i + 1) % len(hull)
    plt.plot([hull[i][0], hull[j][0]], [hull[i][1], hull[j][1]], '-r', linewidth=1)
    plt.pause(0.1)

# Compute the convex hull using QuickHull
hull = quickhull(points)

# Plot all the segments
for i in range(len(hull)):
    j = (i + 1) % len(hull)
    plt.plot([hull[i][0], hull[j][0]], [hull[i][1], hull[j][1]], '-r', linewidth=1)
    plt.pause(0.1)

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