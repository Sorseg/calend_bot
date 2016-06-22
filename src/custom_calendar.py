from calendar import TextCalendar
import re


class BracketCalendar(TextCalendar):

    def formatmonth(self, theyear, themonth, w=0, l=0, day=None):
        w = max(2, w)
        l = max(1, l)
        s = ' '+self.formatmonthname(theyear, themonth, 7 * (w + 1) - 1)
        s = s.rstrip()
        s += '\n' * l
        s += ' ' + self.formatweekheader(w).rstrip()
        s += '\n' * l
        day_re = re.compile(r'\s?\b{}\b\s?'.format(day))
        for week in self.monthdays2calendar(theyear, themonth):
            week_str = ' ' + self.formatweek(week, w).rstrip()
            s += day_re.sub('[{}]'.format(day), week_str)
            s += '\n' * l
        return s
