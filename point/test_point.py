import unittest

from point import Point


class PointTests(unittest.TestCase):

    """Tests for Point."""

    def test_attributes(self):
        point = Point(1, 2, 3)
        self.assertEqual((point.x, point.y, point.z), (1, 2, 3))
        point.x = 4
        self.assertEqual(point.x, 4)

    def test_string_representation(self):
        point = Point(1, 2, 3)
        self.assertEqual(str(point), 'Point(x=1, y=2, z=3)')
        self.assertEqual(repr(point), 'Point(x=1, y=2, z=3)')
        point.y = 4
        self.assertEqual(str(point), 'Point(x=1, y=4, z=3)')
        self.assertEqual(repr(point), 'Point(x=1, y=4, z=3)')

    def test_equality_and_inequality(self):
        p1 = Point(1, 2, 3)
        p2 = Point(1, 2, 4)
        p3 = Point(1, 2, 3)
        self.assertNotEqual(Point(1, 2, 3), Point(1, 2, 4))
        self.assertEqual(Point(1, 2, 3), Point(1, 2, 3))
        self.assertFalse(Point(1, 2, 3) != Point(1, 2, 3))
        self.assertNotEqual(p1, p2)
        self.assertEqual(p1, p3)
        p3.x, p3.z = p3.z, p3.x
        self.assertNotEqual(p1, p3)
        self.assertTrue(p1 != p3)
        self.assertFalse(p1 == p3)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_shifting(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        p3 = p2 + p1
        p4 = p3 - p1
        self.assertEqual((p3.x, p3.y, p3.z), (5, 7, 9))
        self.assertEqual((p4.x, p4.y, p4.z), (p2.x, p2.y, p2.z))

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_scale(self):
        p1 = Point(1, 2, 3)
        p2 = p1 * 2
        self.assertEqual((p2.x, p2.y, p2.z), (2, 4, 6))
        p3 = 3 * p1
        self.assertEqual((p3.x, p3.y, p3.z), (3, 6, 9))

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_iterable_point(self):
        point = Point(x=1, y=2, z=3)
        x, y, z = point
        self.assertEqual((x, y, z), (1, 2, 3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
