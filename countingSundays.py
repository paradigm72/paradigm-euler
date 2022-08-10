from lib import calendar


def loopAllDaysInCentury():
    dayInWeek = 1
    firstSundays = 0
    for year in range(1901, 2001):
        firstDaysInMonth = calendar.getFirstDaysInMonth(year)
        for dayInYear in range(1, calendar.daysInYear(year)):
            if dayInWeek == 7:
                if dayInYear in firstDaysInMonth:
                    firstSundays = firstSundays + 1
                dayInWeek = 1
            else:
                dayInWeek = dayInWeek + 1
        print "As of", year, ", count is", firstSundays
    print "Final count of first Sundays:", firstSundays


loopAllDaysInCentury()
