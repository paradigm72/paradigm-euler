import time

# Constants
GRID_WIDTH = 2
GRID_HEIGHT = 2
PRINT_MODE = 1

validPathCount = 0


def metaAlgo(maxLength):
	global PRINT_MODE
	PRINT_MODE = 0	
	for length in range(maxLength):
		t1 = time.clock()
		initAlgo(length,length)
		t2 = time.clock()
		print "[Length: ",length,"] [Time: ",round(t2-t1, 5),"]"

def initAlgo(widthArg, heightArg):	
	global GRID_WIDTH
	global GRID_HEIGHT
	global validPathCount
	GRID_WIDTH = widthArg
	GRID_HEIGHT = heightArg	
	validPathCount = 0	
	stepForward(0, 0, [], 0, "")
	print validPathCount
	return validPathCount

def stepForward(x, y, parentVisitedCells, validPaths, pathString):
	global validPathCount  # (Prevent creating a new stack level for validPathCount)
	
	# Quit if this cell had already been visited previously on this path
	if parentVisitedCells.count([x, y]):
		return 0
		
	# Otherwise, do list copy to create a unique fork of the visited cell list
	myVisitedCells = list(parentVisitedCells)
	
	# If we reached the end, increment the number of valid paths and quit
	if x==GRID_WIDTH and y==GRID_HEIGHT:
		validPathCount+=1
		if PRINT_MODE==1:
			print "Path #",validPathCount," :",pathString
	
	# If there is room to the right, go right
	if x < GRID_WIDTH:
		# Mark that this cell was visited on this path
		myVisitedCells.append([x, y]);
		stepForward(x+1, y, myVisitedCells, validPaths, pathString+"1")
		
	# If there is room down, go down
	if y < GRID_HEIGHT:
		# Mark that this cell was visited on this path
		myVisitedCells.append([x, y]);
		stepForward(x,y+1, myVisitedCells, validPaths, pathString+"0")
	