def onSegment(p, q, r):
    # Given three collinear points p, q, r, the function checks if
    # point q lies on line segment 'pr'
    px, py = p
    qx, qy = q
    rx, ry = r

    if ((qx <= max(px, rx)) and (qx >= min(px, rx)) and
            (qy <= max(py, r[1])) and (qy >= min(py, ry))):
        return True
    return False


def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
    px, py = p
    qx, qy = q
    rx, ry = r

    val = (float(qy - py) * (rx - qx)) - (float(qx - px) * (ry - qy))
    if val > 0:
        # Clockwise orientation
        return 1
    elif val < 0:
        # Counterclockwise orientation
        return 2
    else:
        # Collinear orientation
        return 0


def doIntersect(p1, q1, p2, q2):
    # see https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/ for more info
    # The main function that returns true if
    # the line segment 'p1q1' and 'p2q2' intersect.
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2) and (o3 != o4):
        return True

    # Special Cases

    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if (o1 == 0) and onSegment(p1, p2, q1):
        return True

    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if (o2 == 0) and onSegment(p1, q2, q1):
        return True

    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if (o3 == 0) and onSegment(p2, p1, q2):
        return True

    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if (o4 == 0) and onSegment(p2, q1, q2):
        return True

    # If none of the cases
    return False

p1 = (1, 1)
q1 = (4, 1)
p2 = (1, 2)
q2 = (4, 2)

if doIntersect(p1, q1, p2, q2):
    print("Yes")
else:
    print("No")

from testing import plotTwoLines
plotTwoLines(p1, p2, q1, q2)