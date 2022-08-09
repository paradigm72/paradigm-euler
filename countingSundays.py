from lib import calendar


def loopAllDaysInCentury():
    dayInWeek = 1
    # get the list of first days of each month, by day-in-year number
    for year in range(1901, 2000):
        for dayInYear in range(1, calendar.daysInYear(year)):
            # if this is a Sunday, check whether it's in the list
            # if so, increment counter and reset dayInWeek to 1
            # otherwise increment dayInWeek = dayInWeek + 1
            pass

