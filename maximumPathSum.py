

def buildPyramidArray(pyramidArray):
    pyramidArray[0] =                                [75]
    pyramidArray[1] =                              [95, 64]
    pyramidArray[2] =                            [17, 47, 82]
    pyramidArray[3] =                          [18, 35, 87, 10]
    pyramidArray[4] =                        [20, 4, 82, 47, 65]
    pyramidArray[5] =                      [19, 1, 23, 75, 3, 34]
    pyramidArray[6] =                    [88, 2, 77, 73, 7, 63, 67]
    pyramidArray[7] =                   [99, 65, 4, 28, 6, 16, 70, 92]
    pyramidArray[8] =                 [41, 41, 26, 56, 83, 40, 80, 70, 33]
    pyramidArray[9] =               [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
    pyramidArray[10] =            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
    pyramidArray[11] =          [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
    pyramidArray[12] =        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
    pyramidArray[13] =      [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
    pyramidArray[14] =    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]


def isValidStep(pyramidArray,startX,startY,endX,endY):

    if len(pyramidArray[endY]) - 1 < endX:
        return False     #off the right edge
    if endX < 0:
        return False     #off the left edge

    if startY > endY - 1:
        return False      #too far down - sanity check
    if (startX - endX) > 0:
        return False      #too far left
    if (startX - endX) < -2:
        return False      #too far right

    return True   #otherwise, it's a valid step


