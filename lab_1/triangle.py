from math import sqrt, acos, pi

EPS = 1e-8

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



