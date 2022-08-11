from lib import calendar


def loopAllDaysInCentury():
    dayInWeek = 2  # for 1901, the first is Tuesday (problem def. is misleading)
    firstSundays = 0
    for year in range(1901, 2001):
        firstDaysInMonth = calendar.getFirstDaysInMonth(year)
        for dayInYear in range(1, calendar.daysInYear(year) + 1):
            if dayInWeek == 7:
                if dayInYear in firstDaysInMonth:
                    firstSundays = firstSundays + 1
                    print year, "Sunday, day number", dayInYear, "was a first of the month"
                else:
                    print year, "Sunday, day number", dayInYear, "was not a first of the month"
                dayInWeek = 1
            else:
                dayInWeek = dayInWeek + 1
        print "As of", year, ", count is", firstSundays
    print "Final count of first Sundays:", firstSundays


loopAllDaysInCentury()
