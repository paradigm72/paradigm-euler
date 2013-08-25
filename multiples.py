def sumFast():
	sumSoFar = 0
	i = 3
	while (i<1000):
		sumSoFar += i
		i += 3
	i = 5
	while (i<1000):
		sumSoFar += i
		i += 5
	print sumSoFar
		
		
def sumNoRepeats():
	sumSoFar = 0
	i = 1
	while (i<1000):
		if ((i % 3) == 0) or ((i % 5) == 0):
			sumSoFar += i
		i += 1
	print sumSoFar
	
# have to know that (n/2)*(n+1) is the arithmetic series 1+2+3+4+5+...+n
def sumElegant(maxNum):
	totalSum = 0
	
	lastTerm = maxNum // 3
	totalSum += 3 * (lastTerm * (lastTerm + 1) / 2)
	
	lastTerm = maxNum // 5
	totalSum += 5 * (lastTerm * (lastTerm + 1) / 2)
	
	# subtract out the series for the union (this is the fix for sumFast() above too)
	lastTerm = maxNum // 15
	totalSum -= 15 * (lastTerm * (lastTerm + 1) / 2)
	
	print totalSum

#Modularity
def seriesToMax(multiple,maxNum):
    return multiple * ((maxNum // multiple) * ((maxNum // multiple) +1 ) / 2)

def sumModular(maxNum):
    totalSum = 0
    totalSum += seriesToMax(3,maxNum)
    totalSum += seriesToMax(5,maxNum)
    totalSum -= seriesToMax(15,maxNum)
    print totalSum

sumModular(999)