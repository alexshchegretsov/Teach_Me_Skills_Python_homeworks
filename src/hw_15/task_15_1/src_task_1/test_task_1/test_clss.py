import unittest
from task_15_1.src_task_1.classes_task_1.clss import MyTime


class LogicOperationsMyTime(unittest.TestCase):
    """Logic tests"""

    def setUp(self):
        self.time_1 = MyTime(13, 7, 11)
        self.time_2 = MyTime(1, 1, 5)
        self.time_3 = MyTime(13, 7, 11)

    def test_eq(self):
        """Equal"""
        self.assertEqual(self.time_1, self.time_3)

    def test_ne(self):
        """Not equal"""
        self.assertNotEqual(self.time_1, self.time_2)

    def test_le(self):
        """Less equal"""
        self.assertLessEqual(self.time_2, self.time_3)

    def test_ge(self):
        """Great equal"""
        self.assertGreaterEqual(self.time_3, self.time_1)

    def test_lt(self):
        """Less then"""
        self.assertLess(self.time_2, self.time_3)

    def test_gt(self):
        """Greater than"""
        self.assertGreater(self.time_3, self.time_2)

    def test_isinstance(self):
        """Is instance"""
        self.assertIsInstance(self.time_2, MyTime)


class CalcMyTime(unittest.TestCase):
    """Tests arithmetic methods"""

    def setUp(self):
        self.time_1 = MyTime(0, 0, 1)
        self.time_2 = MyTime(23, 59, 59)
        self.time_3 = MyTime(24, 0, 0)

    def test_add(self):
        """Two objects addition"""
        self.assertEqual(self.time_1 + self.time_2, MyTime(24, 0, 0))

    def test_sub(self):
        """Two objects substraction"""
        self.assertEqual(self.time_3 - self.time_2, MyTime(0, 0, 1))

    def test_mult(self):
        """Two objects multiply"""
        self.assertEqual(self.time_2 * 2, MyTime(47, 59, 58))


class MethodsMyTime(unittest.TestCase):
    """Tests conversion methods"""

    def test_time_to_seconds(self):
        """Turns time to seconds"""
        res = MyTime(0, 50, 1).time_to_seconds()
        res_2 = MyTime(0, 0, 0).time_to_seconds()
        res_3 = MyTime(1000, 0, 200).time_to_seconds()
        self.assertEqual(res, 3001)
        self.assertEqual(res_2, 0)
        self.assertEqual(res_3, 3600200)

    def test_seconds_to_time(self):
        """Turns seconds to time"""
        res = MyTime().seconds_to_time(3600200)
        res_2 = MyTime().seconds_to_time(1)
        self.assertEqual(res, (1000, 3, 20))
        self.assertEqual(res_2, (0, 0, 1))


if __name__ == '__main__':
    unittest.main()
