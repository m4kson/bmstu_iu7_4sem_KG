from math import sqrt, acos, pi

EPS = 1e-6

def is_triangle(side_size_a, side_size_b, side_size_c):
    if abs(side_size_a + side_size_b - side_size_c) < EPS or abs(side_size_a + side_size_c - side_size_b) < EPS or abs(side_size_b + side_size_c - side_size_a) < EPS:
        return False
    return True

