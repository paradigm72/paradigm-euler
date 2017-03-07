import math


def lettersPerOnesPlace(number):
    if number == 1:
        return 3   #one
    if number == 2:
        return 3   #two
    if number == 3:
        return 5   #three
    if number == 4:
        return 4   #four
    if number == 5:
        return 4   #five
    if number == 6:
        return 3   #six
    if number == 7:
        return 5   #seven
    if number == 8:
        return 5   #eight
    if number == 9:
        return 4   #nine
    if number == 0:
        return 0   #we never actually say zero


def lettersPerTensPlace(tens, ones, appendOnesLetters):
    if tens == 1:
        if ones == 1:
            appendOnesLetters[0] = False
            return 6     #eleven
        if ones == 2:
            appendOnesLetters[0] = False
            return 6     #twelve
        if ones == 3:
            appendOnesLetters[0] = False
            return 8     #thirteen
        if ones == 5:
            appendOnesLetters[0] = False
            return 7     #fifteen
        if ones == 0:
            appendOnesLetters[0] = False
            return 3     #ten
        else:
            return 4     # "teen"
    if tens == 2:
        return 6     #twenty
    if tens == 3:
        return 6     #thirty
    if tens == 4:
        return 5     #forty
    if tens == 5:
        return 5     #fifty
    if tens == 8:
        return 6     #eighty
    else:
        return (lettersPerOnesPlace(tens) + 2)   #<onesplace>ty



def lettersPerNumber(number):
    ones = number % 10
    tens = (number - ones) % 100
    hundreds = number - tens - ones

    if number == 101:
        junk = 1

    appendOnesLetters = [True]
    if hundreds > 0:
        hLetters = lettersPerOnesPlace(hundreds // 100)
    else:
        hLetters = 0

    if tens > 0:
        tLetters = lettersPerTensPlace(tens // 10,ones,appendOnesLetters)
    else:
        tLetters = 0

    if appendOnesLetters[0]:
        oLetters = lettersPerOnesPlace(ones)
    else:
        oLetters = 0

    if hLetters > 0:
        if tLetters > 0 or oLetters > 0:
            hLetters += 10  #"hundred and"
        else:
            hLetters += 7  #"hundred

    totalLetters = hLetters + tLetters + oLetters
    return totalLetters


def lettersForAllNumbersUpTo(finalNumber):
    runningTotal = 0
    for i in range(1,finalNumber):
        runningTotal += lettersPerNumber(i)
        print i," has ",lettersPerNumber(i)," letters."

    print "1000 has  11  letters."
    print "Total number of letters up to ",finalNumber,": ",runningTotal+11

lettersForAllNumbersUpTo(1000)