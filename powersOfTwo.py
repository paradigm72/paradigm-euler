import atomicOperators
import time

def printExponents(base,maxExponent):
    currentVal = base
    for i in range(1,maxExponent+1):
        print  i,"  ",currentVal,"  ",atomicOperators.sumDigits(currentVal,10)
        currentVal = currentVal * base


def getFinalMultiple(base,maxExponent):
    currentVal = base
    for i in range(1,maxExponent):
        currentVal = currentVal * base
    return currentVal

#printExponents(2,1000);
#print getFinalMultiple(2,1000);
#print atomicOperators.sumDigits(21430172143725346418968500981200036211228096234110672148875007767407021022498722449863967576313917162551893458351062936503742905713846280871969155149397149607869135549648461970842149210124742283755908364306092949967163882534797535118331087892154125829142392955373084335320859663305248773674411336138752,10);
print atomicOperators.sumDigits(getFinalMultiple(2,1000),10);