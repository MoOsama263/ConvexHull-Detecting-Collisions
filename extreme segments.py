import random
import matplotlib.pyplot as plt
from typing import List, Set, Tuple

def compute_extreme_segments(X: List[Tuple[float, float]]) -> Set[Tuple[Tuple[float, float], Tuple[float, float]]]:
    extreme_segments = set()
    other_segments = []
    for i in range(len(X)):
        for j in range(i+1, len(X)):
            same_halfplane = True
            for k in range(len(X)):
                if k != i and k != j:
                    if (X[k][0] - X[i][0]) * (X[j][1] - X[i][1]) > (X[k][1] - X[i][1]) * (X[j][0] - X[i][0]):
                        same_halfplane = False
                        break
            if same_halfplane:
                extreme_segments.add((X[i], X[j]))
            else:
                other_segments.append((X[i], X[j]))
    return extreme_segments, other_segments

# Generate random points
points = []
for i in range(30):
    points.append((random.randint(1, 20), random.randint(1, 20)))

# Plot the points
plt.scatter([p[0] for p in points], [p[1] for p in points], s=10)

# Find the extreme segments and other segments
extreme_segments, other_segments = compute_extreme_segments(points)

# Turn off interactive mode
plt.ioff()

# Plot the other segments
for s in other_segments:
    plt.plot([s[0][0], s[1][0]], [s[0][1], s[1][1]], '-g', linewidth=1)

# Plot the extreme segments
for s in extreme_segments:
    plt.plot([s[0][0], s[1][0]], [s[0][1], s[1][1]], '-r', linewidth=1)

# Turn on interactive mode
plt.ion()

# Wait for user to close the plot window
while plt.get_fignums():
    if plt.waitforbuttonpress(0.01):
        plt.close()
        break

plt.show()
