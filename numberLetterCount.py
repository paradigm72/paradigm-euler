import math


def lettersPerOnesPlace(number):
    if number == 1:
        return 3
    if number == 2:
        return 3
    if number == 3:
        return 5
    if number == 4:
        return 4
    if number == 5:
        return 4
    if number == 6:
        return 3
    if number == 7:
        return 5
    if number == 8:
        return 5
    if number == 9:
        return 4
    if number == 0:
        return 4


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
    else:
        return (lettersPerOnesPlace(tens) + 2)   #<onesplace>ty



def lettersPerNumber(number):
    ones = number % 10
    tens = (number - ones) % 100
    hundreds = number - tens - ones

    appendOnesLetters = [True]
    hLetters = lettersPerOnesPlace(hundreds // 100)
    tLetters = lettersPerTensPlace(tens // 10,ones,appendOnesLetters)
    if appendOnesLetters[0]:
        oLetters = lettersPerOnesPlace(ones)
    else:
        oLetters = 0

    if hLetters > 0:
        hLetters += 10  #"hundred and"

    totalLetters = hLetters + tLetters + oLetters
    print "Letters for number ",number,": ",totalLetters,"."


lettersPerNumber(142)
print "One hundred and forty-two"
lettersPerNumber(712)
print "Seven hundred and twelve"