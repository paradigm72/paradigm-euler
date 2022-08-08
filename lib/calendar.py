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

