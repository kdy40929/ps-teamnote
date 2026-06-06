from functools import cmp_to_key

def cross(p1, p2, p3, p4):
    # p1 -> p2 / p3 -> p4
    return (p2[0]-p1[0])*(p4[1]-p3[1]) - (p4[0]-p3[0])*(p2[1]-p1[1])

def di_area(pts):
    s = 0
    for i in range(len(pts)):
        s += pts[i][0]*pts[i-1][1] - pts[i-1][0]*pts[i][1]
    return abs(s)

def intersect(p1, p2, q1, q2):
    # p1 - p2 / q1 - q2
    a = cross(p1, p2, p1, q1) * cross(p1, p2, p1, q2)
    b = cross(q1, q2, q1, p1) * cross(q1, q2, q1, p2)
    if a == b == 0:
        return max(p1, p2) >= min(q1, q2) and max(q1, q2) >= min(p1, p2)
    return a <= 0 and b <= 0

def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def comp(base, p1, p2):
    cp = cross(base, p1, base, p2)
    if cp > 0: return -1
    if cp < 0: return 1
    return 1 if dist(base, p1) > dist(base, p2) else -1

def convex_hull(points):
    base = min(points, key = lambda x: (x[1], x[0]))
    sorted_points = sorted(points, key=cmp_to_key(lambda p1, p2: comp(base, p1, p2)))
    hull = []
    for p in sorted_points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], hull[-2], p) <= 0:
            hull.pop()
        hull.append(p)
    return hull

def check_inconvex(pg, point, kind):
    # include edge if kind == 1
    if kind == 1:
        if cross(pg[0], pg[1], pg[0], point) < 0: return 0
        if cross(pg[0], pg[-1], pg[0], point) > 0: return 0
        left, right = 0, len(pg) - 1
        while left + 1 < right:
            mid = (left + right)//2
            if cross(pg[0], pg[mid], pg[0], point) >= 0:
                left = mid
            else: right = mid
        return cross(pg[left], point, point, pg[right]) <= 0
    else:
        if cross(pg[0], pg[1], pg[0], point) <= 0: return 0
        if cross(pg[0], pg[-1], pg[0], point) >= 0: return 0
        left, right = 0, len(pg) - 1
        while left + 1 < right:
            mid = (left + right)//2
            if cross(pg[0], pg[mid], pg[0], point) > 0:
                left = mid
            else: right = mid
        return cross(pg[left], point, point, pg[right]) < 0

def rot_calipers(hull):
    # find a maximum distance among points of hull
    maxdst = 0
    j = 1
    n = len(hull)
    p1, p2 = hull[0], hull[1]
    for i in range(n):
        while j < 2*n and cross(hull[i], hull[(i+1)%n], hull[j%n], hull[(j+1)%n]) >= 0:
            tmp = dist(hull[i], hull[j%n])
            if tmp > maxdst:
                maxdst = tmp
                p1, p2 = hull[i], hull[j%n]
            j += 1
        tmp = dist(hull[i], hull[j%n])
        if tmp > maxdst:
            maxdst = tmp
            p1, p2 = hull[i], hull[j%n]
    return [p1, p2]