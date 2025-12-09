import sys

import matplotlib.pyplot as plt

raw_input = sys.stdin.read().split()
coords = [tuple(map(int, line.split(","))) for line in raw_input]
max_rect = 0

""" Part 1
for i in range(len(coords)):
    x1, y1 = coords[i]
    for j in range(i + 1, len(coords)):
        x2, y2 = coords[j]
        max_rect = max(max_rect, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
"""
# First idea: for each red tile, determine the maximum distance we can stay
# within the wrapped shape for each of the 4 cardinal directions
# From the input format, we get 2/4 for free. When the corner is locally 'convex',
# we don't have to compute anything else. Only when the corner is locally 'concave'
# do we need to compute all four directions. Possible improvement: only calculate
# extra information for concave corners when necessary

""" Visualization
x, y = zip(*coords)
plt.plot(x, y)
plt.show()

Conclusion: The figure is divided into upper and lower hemispheres, we can perform
individual calculations on each hemisphere.
Furthermore, if we choose both corners to be on the circumference on the circle, the resulting
rectangle almost always (except for vanishingly small cases) escapes the circle.
Therefore, we almost certainly want to only consider rectangles that use the interior points
as one corner. Thus, for each hemisphere we only have to check each point against a single point!

The orientation of the figure is counter-clockwise, and our special points are:
    94737,50273 (upper hemisphere)
    94737,48494 (lower hemisphere)

If these points are used as a corner of a rectangle, there is a bound on the size of the vertical line
so we can further eliminate many points from consideration.

To determine if a point can be used as a valid corner, we need the edge drawn vertically to the equator
to stay within the circle. Create a list of horizontal line segments, and we can check interesection of the
vertical line segment with these horiztonal segments. Any intersection besides interior endpoint = invalid
"""


def rectsize(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def intersect(l1, l2):
    if l1[0] == l2[0] or l1[0] == l2[1]:
        return False  # point on segment, ignore
    if l2[0][0] > l2[1][0]:  # rightward edge, wrong orientation
        if l2[1][0] <= l1[0][0] <= l2[0][0] and l1[1][1] <= l2[0][1] <= l1[0][1]:
            return True
        return False
    else:
        if l2[0][0] < l1[0][0] <= l2[1][0] and l1[1][1] <= l2[0][1] <= l1[0][1]:
            return True
    return False


horizontal_segs = []  # (x1, y1, x2, y2)
for i in range(1, len(coords)):
    if coords[i - 1][1] == coords[i][1]:
        horizontal_segs.append((coords[i - 1], coords[i]))  # first point is 'interior'

for point in coords:
    altitude = (point, (point[0], 50273))
    valid = True
    for seg in horizontal_segs:
        if intersect(altitude, seg):
            valid = False
            break
    if valid:
        print(f"Candidate found: {point}")
        max_rect = max(max_rect, rectsize(point, (94737, 50273)))

# TODO: Repeat analysis with lower cands, answer should be there.
# Too low: 1527936636
# Too high: 1806816974

# upper_pts = [point for point in coords if point[1] > 50273]
# upper_cands =
"""
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
available = [] # corresponds with dirs above
for i in range(len(coords)):
"""

print(max_rect)
