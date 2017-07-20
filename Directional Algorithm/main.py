oo = 1e9
allPOIs = []
# this is the algorithm code for the alarm hub

# Ctrl-f "revisit" to find issues/potentially irrelevant code

class PointOfInterest:
    # constructor of an POI
    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.left = 0
        self.right = 0
        self.middle = 0
        self.leftLED = 0
        self.rightLED = 0
        self.middleLED = 0
        self.buzzer = 0
        self.nextPOI = 0

    # setters for POIs
    def setLeft(self, POI):
        self.left = POI

    def setRight(self, POI):
        self.right = POI

    def setMiddle(self, POI):
        self.middle = POI

    def setAll(self, left, right, middle):
        self.setLeft(left)
        self.setRight(right)
        self.setMiddle(middle)

    # revisit necessity and use of this function
    def setNext(self, POI):
        self.nextPOI = POI

    def setVisited(self, boolean):
        self.visited = boolean

    # getters for POIs
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getMiddle(self):
        return self.middle

    def getID(self):
        return self.id

    def getType(self):
        return self.type

    # revisit necessity and use of this function
    def getNext(self):
        return self.nextPOI

    def getVisited(self):
        return self.visited

def resetVisited():
    for POI in allPOIs:
        POI.setVisited(False)



# probably don't need "length" or POIFrom parameters revisit
def setPath(POI, length, POIFrom, thisPath, visited):

    print POI.getID()

    if(POI.getType() == "wall") or (POI.getID() == 0):
        return visited

    visited[POI.getID()] = True

    if(POI.getType() == "exit"):
        return visited


    # base case
    if (POI.getLeft().getType() != "wall") and (POI.getLeft().getType() == "exit"):
        POI.setNext(POI.getLeft())
        # POI.getLeft().setVisited(True)
        visited[POI.getLeft().getID()] = True
        return visited
    elif (POI.getRight().getType() != "wall") and (POI.getRight().getType() == "exit"):
        POI.setNext(POI.getRight())
        visited[POI.getRight().getID()] = True
        return visited
    elif (POI.getMiddle().getType() != "wall") and (POI.getMiddle().getType() == "exit"):
        POI.setNext(POI.getMiddle())
        visited[POI.getMiddle().getID()] = True
        return visited

    # set the path lengths for the left direction
    # we do not want to go back the way we came so we have a check for that.
    if(POI.getLeft().getType() != "wall" and visited[POI.getLeft().getID()] == False):
        leftPath = combineArray(visited, setPath(POI.getLeft(), length, POI, thisPath, visited))
    else:
        leftPath = oo

    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(POI.getRight().getType() != "wall" and visited[POI.getRight().getID()] == False):
         rightPath = combineArray(visited, setPath(POI.getRight(), length, POI, thisPath, visited))
    else:
        rightPath = oo

    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(POI.getMiddle().getType() != "wall" and visited[POI.getMiddle().getID()] == False):
         middlePath = combineArray(visited, setPath(POI.getMiddle(), length, POI, thisPath, visited))
    else:
        middlePath = oo

    leftLength = findPathLength(leftPath)
    rightLength = findPathLength(rightPath)
    middleLength = findPathLength(middlePath)


    #find the minimum path, and set the next POI
    if((leftLength < rightLength) and (leftLength < middleLength)):
        POI.setNext(POI.getLeft())
        visited[POI.getLeft().getID()] = True
        return visited
    elif((rightLength < leftLength) and (rightLength < middleLength)):
        POI.setNext(POI.getRight())
        visited[POI.getRight().getID()] = True
        return visited
    elif((middleLength < leftLength) and (middleLength < rightLength)):
        POI.setNext(POI.getMiddle())
        visited[POI.getLeft().getID()] = True
        return visited
    ## if the paths are equal go left cause why not
    elif(rightLength == leftLength and POI.getID() != POIFrom.getLeft().getID()):
        POI.setNext(POI.getLeft())
        visited[POI.getLeft().getID()] = True
        return visited
    else:
        POI.setNext(POI.getMiddle())
        visited[POI.getLeft().getID()] = True
        return visited

# follows a path until it gets to a wall or exit
def followPath(POI, myPath):

    if ((POI ==0) or (POI.getType() == "wall")):
        return

    if(POI.getID() == 0):
        return

    myPath += [POI]

    # don't wanna go into a wall, buddy (you right)
    if((POI.getNext() == 0) or (POI.getNext().getType() == "wall")):
        return

    # follow the next POI in the path
    followPath(POI.getNext(), myPath)



def fireAlarm(POI, visited):
    print "Setting off alarm " + str(POI.getID())
    setPath(POI.getLeft(), 0, POI, [], visited)
    setPath(POI.getRight(), 0, POI, [], visited)
    setPath(POI.getMiddle(), 0, POI, [], visited)


    leftPath = []
    followPath(POI.getLeft(), leftPath)
    print "left path: " + printPath(leftPath)
    rightPath = []
    followPath(POI.getRight(), rightPath)
    print "right path: " + printPath(rightPath)
    middlePath = []
    followPath(POI.getMiddle(), middlePath)
    print "middle path: " + printPath(middlePath)

    leftLength = findPathLength(leftPath)
    rightLength = findPathLength(rightPath)
    middleLength = findPathLength(middlePath)

    #find the minimum path, and set the next POI
    if((leftLength < rightLength) and (leftLength < middleLength)):
        print "Shortest Path is Left Path"
    elif((rightLength < leftLength) and (rightLength < middleLength)):
        print "Shortest Path is Right Path"
    elif((middleLength < leftLength) and (middleLength < rightLength)):
        print "Shortest Path is Middle Path"
    ## if the paths are equal go left cause why not
    elif(rightLength == leftLength and POI.getID() != POIFrom.getLeft().getID()):
        print "Shortest Path is Left Path"
    else:
        print "Shortest Path is Left Path"




def printPath(thisPath):
    pathString = ""
    if (len(thisPath) == 0):
        return "none"
    for POI in thisPath:
        pathString += (str(POI.getType()) + str(POI.getID()) + " -> ")
    return pathString

def findPathLength(thisPath):
    if(thisPath == oo or len(thisPath) == 0):
        pathLength = oo
    else:
        pathLength = len(thisPath)
    return pathLength

def combineArray(vis1, vis2):
    newVis = []
    if(len(vis1) != len(vis2)):
        return
    i = 0
    for val in vis1:
        if((vis1[i] == True) or (vis2[i] == True)):
            newVis += [True]
        else:
            newVis+= [False]
        i+=1

    return newVis


# main function
def main():

    allPOIs = []
    visited = []

    # set up POI as wall
    allPOIs += [PointOfInterest(0, "wall")]
    wall = allPOIs[0]
    # Set up five POIs as type alarm
    for i in range(1, 6):
        tempPOI = PointOfInterest(i, "alarm")
        allPOIs += [tempPOI]

    # Set up 3 POIs as type exit
    for i in range(6, 9):
        allPOIs += [PointOfInterest(i, "exit")]


    # initialize the connections from one alarm to another
    allPOIs[1].setAll(wall,  allPOIs[8], wall)
    allPOIs[2].setAll(allPOIs[1], allPOIs[3], wall)
    allPOIs[3].setAll(wall, allPOIs[1], wall)
    allPOIs[4].setAll(wall, allPOIs[5], allPOIs[3])
    allPOIs[5].setAll(wall, allPOIs[7], wall)

    for POI in allPOIs:
        visited += [False]

    fireAlarm(allPOIs[4], visited)





if __name__ == "__main__":
    main()
