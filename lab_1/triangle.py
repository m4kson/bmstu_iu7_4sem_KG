from math import sqrt, acos, pi
from class_point import Point

EPS = 1e-8

class Triangle:
    def __init__(self, point1, point2, point3):
        self.A = point1
        self.B = point2
        self.C = point3

def is_triangle(point1, point2, point3):
    if find_side_size(point1, point2) + find_side_size(point1, point3) <= find_side_size(point2, point3) or \
        find_side_size(point1, point3) + find_side_size(point2, point3) <= find_side_size(point1, point2) or \
            find_side_size(point2, point3) + find_side_size(point1, point2) <= find_side_size(point1, point3):
            return False
    return True

def find_side_size(point1, point2):
    return sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))

def is_stupid_triangle(point1, point2, point3):
    if not is_triangle:
        return False

    max_size_pow = pow(max(find_side_size(point1, point2), find_side_size(point2, point3), find_side_size(point1, point3)), 2)
    size1_pow = pow(find_side_size(point1, point2), 2)
    size2_pow = pow(find_side_size(point2, point3), 2)
    size3_pow = pow(find_side_size(point1, point3), 2)

    arr = [size1_pow, size2_pow, size3_pow]
    sum = 0
    for i in range(3):
        if arr[i] != max_size_pow:
            sum += arr[i]

    if max_size_pow > sum:
        return True

    return False


def find_point_near_stupid_corner(point1, point2, point3):
    size1 = find_side_size(point1, point2)
    size2 = find_side_size(point2, point3)
    size3 = find_side_size(point1, point3)

    max_side = max(size1, size2, size3)

    if max_side == size1:
        return point3
    elif max_side == size2:
        return point1
    else:
        return point2

def find_corner(point1, point2):
    pass

def line_equation(x, point1, point2):
    try:
        return (x - point1.x) * (point2.y - point1.y) / (point2.x - point1.x) + point1.y
    except:
        return None

def line_equation_y(y, point1, point2):
    try:
        x = (y - point1.y) * (point2.x - point1.x) / (point2.y - point1.y) + point1.x
        return x
    except:
        return None

def is_pryamoi(point1, point2, point3):
    pass

def find_cos(point1, point2):
    pointY = Point(0, line_equation(0, point1, point2))
    pointX = Point(line_equation_y(0, point1, point2), 0)

    if pointY.y == None:
        return 0
    elif pointX.x == None:
        return 1

    cos = pointX.x / find_side_size(pointY, pointX)

    return cos

def find_all_stupid_triangles(set):
    triangles = []
    for i in range(len(set)):
        for j in range(i + 1, len(set)):
            for k in range(j + 1, len(set)):
                if is_stupid_triangle(set[i], set[j], set[k]):
                    triangles.append(Triangle(set[i], set[j], set[k]))

    return triangles


def find_ans(setA, setB):
    trianglesA = find_all_stupid_triangles(setA)
    trianglesB = find_all_stupid_triangles(setB)

    ans = [trianglesA[0], trianglesB[0]]
    mincos = 1

    for i in range(len(trianglesA)):
        dot1 = find_point_near_stupid_corner(trianglesA[i].A, trianglesA[i].B, trianglesA[i].C)
        for j in range(len(trianglesB)):
            dot2 = find_point_near_stupid_corner(trianglesB[j].A, trianglesB[j].B, trianglesB[j].C)
            if find_cos(dot1, dot2) < mincos:
                mincos = find_cos(dot1, dot2)
                ans[0] = trianglesA[i]
                ans[1] = trianglesB[j]

    return ans


