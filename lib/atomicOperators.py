def sumDigits(number,base):
    try:
        base = int(base)
    except:
        base = 10

    curVal = number
    curSum = 0
    while curVal >= 1:
        remainder = curVal % base
        curSum += remainder
        curVal = int(curVal / base)
    return curSum

def elegantSumDigits(number):
    curSum = 0
    for digit in str(number):
        curSum += int(digit);
    return curSum



#print sumDigits(1000000,10);