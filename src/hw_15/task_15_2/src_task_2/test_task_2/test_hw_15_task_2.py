import unittest
from math import pi
from task_15_2.src_task_2.classes_task_2.clss_2 import (
    Point,
    Figure,
    Circle,
    Triangle,
    Square,
)


class distanceFigure(unittest.TestCase):

    def setUp(self):
        self.point_1 = Point(2, 4)
        self.point_2 = Point(200, 200)
        self.point_3 = Point(0, 1)
        self.point_4 = Point(1000000, -1000000)

    def test_distance_1(self):
        dist_1 = Figure().calc_dist(self.point_3, self.point_4)
        self.assertEqual(round(dist_1, 1), 1414214.3)

    def test_distance_2(self):
        dist_1 = Figure().calc_dist(self.point_1, self.point_2)
        self.assertEqual(round(dist_1, 1), 278.6)

    def test_distance_3(self):
        dist_1 = Figure().calc_dist(self.point_2, self.point_4)
        self.assertEqual(round(dist_1, 1), 1414213.6)


class calcPerimeter(unittest.TestCase):

    def setUp(self):
        self.point_1 = Point(2, 4)
        self.point_2 = Point(200, 200)
        self.point_3 = Point(0, 1)
        self.point_4 = Point(1000000, -1000000)

    def test_circle_perimeter(self):
        perimeter_1 = Circle(self.point_4, 1).calc_perimeter()
        perimeter_2 = Circle(self.point_4, 0).calc_perimeter()
        perimeter_3 = Circle(self.point_4, -1000000).calc_perimeter()
        self.assertEqual(perimeter_1, 2 * pi)
        self.assertEqual(perimeter_2, 0)
        self.assertEqual(round(perimeter_3, 1), -6283185.3)

    def test_triangle_perimeter(self):
        perimeter = Triangle(self.point_1, self.point_2, self.point_3).calc_perimeter()
        self.assertEqual(round(perimeter, 1), 564.3)

    def test_square_perimeter(self):
        perimeter_1 = Square(self.point_4, self.point_2).calc_perimeter()
        self.assertEqual(round(perimeter_1, 1), 4000000.1)


class calcSquare(unittest.TestCase):

    def setUp(self):
        self.point_1 = Point(2, 4)
        self.point_2 = Point(200, 200)
        self.point_3 = Point(0, 1)
        self.point_4 = Point(1000000, -1000000)
        self.triangle_perimeter = round(Triangle(self.point_1, self.point_2, self.point_3).calc_perimeter(), 1)
        self.square_perimeter = round(Square(self.point_4, self.point_2).calc_perimeter(), 1)

    def test_circle_square(self):
        sq_1 = Circle(self.point_4, 1000).calc_area()
        sq_2 = Circle(self.point_4, 0).calc_area()
        sq_3 = Circle(self.point_4, -1000000).calc_area()
        self.assertEqual(round(sq_1, 1), 3141592.7)
        self.assertEqual(sq_2, 0)
        self.assertEqual(round(sq_3, 1), 3141592653589.8)

    def test_triangle_square(self):
        sq_1 = Triangle(self.point_4, self.point_2, self.point_3).calc_area()
        self.assertEqual(round(sq_1, 1), 199500100.0)

    def test_square_square(self):
        sq_1 = Square(self.point_4,self.point_3).calc_area()
        self.assertEqual(round(sq_1,1),1000001000000.5)
