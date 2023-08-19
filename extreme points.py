import matplotlib
matplotlib.use('TkAgg')
import random
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Generate random points
points = []
for i in range(30):
    points.append([random.randint(1, 20), random.randint(1, 20)])

# Check if a point lies inside a triangle formed by three other points
def point_in_triangle(p, p1, p2, p3):
    # Find the area of triangle formed by p1, p2 and p3
    A = area(p1, p2, p3)

    # Find the area of triangle formed by p, p1 and p2
    A1 = area(p, p1, p2)

    # Find the area of triangle formed by p, p2 and p3
    A2 = area(p, p2, p3)

    # Find the area of triangle formed by p, p3 and p1
    A3 = area(p, p3, p1)

    # Check if sum of A1, A2 and A3 is same as A
    return A == A1 + A2 + A3

# Calculate the area of a triangle formed by three points
def area(p1, p2, p3):
    return abs((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])) / 2.0

# Plot the points
plt.scatter([p[0] for p in points], [p[1] for p in points], s=20)

# Draw the convex hull
hull = ConvexHull([points[i] for i in range(len(points))])
for i in range(len(hull.vertices)):
    p1 = points[hull.vertices[i]]
    p2 = points[hull.vertices[(i+1)%len(hull.vertices)]]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], '-r', linewidth=0.5)

# Remove interior points
extreme = set(range(len(points)))
for i in range(len(points)):
    for j in range(i+1, len(points)):
        for k in range(j+1, len(points)):
            if i != j and i != k and j != k:
                p = points[i]
                p1 = points[j]
                p2 = points[k]
                plt.plot([p[0], p1[0], p2[0], p[0]], [p[1], p1[1], p2[1], p[1]], '-g', linewidth=0.5)
                plt.pause(0.5)
                to_remove = set()
                for l in extreme:
                    if l != i and l != j and l != k:
                        if point_in_triangle(points[l], p, p1, p2):
                            to_remove.add(l)
                if to_remove:
                    extreme.difference_update(to_remove)
                    plt.scatter([points[l][0] for l in to_remove], [points[l][1] for l in to_remove], color='gray')

plt.show()