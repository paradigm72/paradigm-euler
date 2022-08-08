import unittest
from lib import calendar


class MyTestCase(unittest.TestCase):
    def test_leap_years(self):
        self.assertEqual(calendar.isLeapYear(1977), False)
        self.assertEqual(calendar.isLeapYear(1980), True)
        self.assertEqual(calendar.isLeapYear(1900), False)
        self.assertEqual(calendar.isLeapYear(2000), True)
        self.assertEqual(calendar.isLeapYear(6723), False)


if __name__ == '__main__':
    unittest.main()
