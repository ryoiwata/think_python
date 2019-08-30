"""
Chapter 15: Classes and Objects
"""

class Point:
    """
    Represensts a point in 2-D Space
    """

def print_point(point):
    print("{}, {}".format(point.x, point.y))

def distance_between_points(point_1, point_2):
    x_distance = point_2.x - point_1.x
    y_distance = point_2.y - point_1.y
    return (x_distance ** 2 + y_distance ** 2) ** 0.5

class Rectangle:
    """
    Represents a rectangle

    attributes: width, height, corner
    """


point_1 = Point()
point_1.x = 0
point_1.y = 0

point_2 = Point()
point_2.x = 3
point_2.y = 4

print(distance_between_points(point_2, point_1))

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0