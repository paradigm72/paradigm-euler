def isLeapYear(year):
    if ((year % 4) == 0):
        if ((year % 100) == 0):
            if ((year % 400) == 0):
                return True;
            return False;
        return True;
    return False;


def daysInMonth(month, year):
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        return 31
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
    return 30


def getFirstDaysInMonth(year):
    dayNumInMonth = 0
    monthNum = 1
    dayNums = [1]   # start with Jan. 1 as a first day of a month
    daysInYear = 366 if isLeapYear(year) else 365

    for dayNumInYear in range(1, daysInYear):
        dayNumInMonth = dayNumInMonth + 1
        if dayNumInMonth > daysInMonth(monthNum, year):
            monthNum = monthNum + 1
            dayNumInMonth = 1
            dayNums.append(dayNumInYear)
    return dayNums
