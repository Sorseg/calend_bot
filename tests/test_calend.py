from unittest import TestCase

from custom_calendar import BracketCalendar
JUNE = '''\
      June 2016
 Mo Tu We Th Fr Sa Su
        1  2  3  4  5
  6  7  8  9 10 11 12
 13 14 15 16 17 18 19
 20 21 22[23]24 25 26
 27 28 29 30
'''
JUNE_20 = '''\
      June 2016
 Mo Tu We Th Fr Sa Su
        1  2  3  4  5
  6  7  8  9 10 11 12
 13 14 15 16 17 18 19
[20]21 22 23 24 25 26
 27 28 29 30
'''

JUNE_3 = '''\
      June 2016
 Mo Tu We Th Fr Sa Su
        1  2 [3] 4  5
  6  7  8  9 10 11 12
 13 14 15 16 17 18 19
 20 21 22 23 24 25 26
 27 28 29 30
'''


class TestCalend(TestCase):
    maxDiff = None
    def test_current_date(self):
        form = BracketCalendar().formatmonth(2016, 6, day=23)
        self.assertEqual(form, JUNE)

    def test_bracket_case(self):
        form = BracketCalendar().formatmonth(2016, 6, day=20)
        self.assertEqual(form, JUNE_20)

    def test_one_digit(self):
        form = BracketCalendar().formatmonth(2016, 6, day=3)
        self.assertEqual(form, JUNE_3)

