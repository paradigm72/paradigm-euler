import unittest
from lib import calendar


class CalendarTests(unittest.TestCase):
    def testIsLeapYear(self):
        self.assertEqual(calendar.isLeapYear(1977), False)
        self.assertEqual(calendar.isLeapYear(1980), True)
        self.assertEqual(calendar.isLeapYear(1900), False)
        self.assertEqual(calendar.isLeapYear(2000), True)
        self.assertEqual(calendar.isLeapYear(6723), False)

    def testDaysInMonth(self):
        self.assertEqual(calendar.daysInMonth(1, 1974), 31)
        self.assertEqual(calendar.daysInMonth(2, 1980), 29)
        self.assertEqual(calendar.daysInMonth(2, 1981), 28)
        self.assertEqual(calendar.daysInMonth(4, 1981), 30)

if __name__ == '__main__':
    unittest.main()
