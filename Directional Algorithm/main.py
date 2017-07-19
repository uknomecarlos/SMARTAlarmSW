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
        self.nextPOI = 0 #revisit necessity of attribute

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
        return []

    visited[POI.getID()] = True

    if(POI.getType() == "exit"):
        return [POI]


    # base case
    if (POI.getLeft().getType() != "wall") and (POI.getLeft().getType() == "exit"):
        POI.setNext(POI.getLeft())
        # POI.getLeft().setVisited(True)
        visited[POI.getLeft().getID()] = True
        return [POI.getLeft()]
    elif (POI.getRight().getType() != "wall") and (POI.getRight().getType() == "exit"):
        POI.setNext(POI.getRight())
        visited[POI.getRight().getID()] = True
        return [POI.getRight()]
    elif (POI.getMiddle().getType() != "wall") and (POI.getMiddle().getType() == "exit"):
        POI.setNext(POI.getMiddle())
        visited[POI.getMiddle().getID()] = True
        return [POI.getMiddle()]

    # set the path lengths for the left direction
    # we do not want to go back the way we came so we have a check for that.
    if(POI.getLeft().getType() != "wall" and visited[POI.getLeft().getID()] == False):
        leftPath = setPath(POI.getLeft(), length, POI, thisPath, visited)
    else:
        leftPath = oo

    #if(POI.getLeft() != 0 and POIFrom.getID() != POI.getLeft().getID()):
    #     leftPath = setPath(POI.getLeft(), length, POI) + 1
    #else:
     #   leftPath = oo



    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(POI.getRight().getType() != "wall" and visited[POI.getRight().getID()] == False):
         rightPath = setPath(POI.getRight(), length, POI, thisPath, visited)
    else:
        rightPath = oo

    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(POI.getMiddle().getType() != "wall" and visited[POI.getMiddle().getID()] == False):
         middlePath = setPath(POI.getMiddle(), length, POI, thisPath, visited)
    else:
        middlePath = oo

    leftLength = findPathLength(leftPath)
    rightLength = findPathLength(rightPath)
    middleLength = findPathLength(middlePath)


    #find the minimum path, and set the next POI
    if((leftLength < rightLength) and (leftLength < middleLength)):
        POI.setNext(POI.getLeft())
        visited[POI.getLeft().getID()] = True
        return [POI.getLeft()] + leftPath
    elif((rightLength < leftLength) and (rightLength < middleLength)):
        POI.setNext(POI.getRight())
        visited[POI.getRight().getID()] = True
        return [POI.getRight()] + rightPath
    elif((middleLength < leftLength) and (middleLength < rightLength)):
        POI.setNext(POI.getMiddle())
        visited[POI.getLeft().getID()] = True
        return [POI.getMiddle()] + middlePath
    ## if the paths are equal go left cause why not
    elif(rightLength == leftLength and POI.getID() != POIFrom.getLeft().getID()):
        POI.setNext(POI.getLeft())
        visited[POI.getLeft().getID()] = True
        return [POI.getLeft()] + leftPath
    else:
        POI.setNext(POI.getMiddle())
        visited[POI.getLeft().getID()] = True
        return [POI.getMiddle()] + middlePath


# follows a path until it gets to a wall or exit
def followPath(POI):

    if (POI == 0):
        return

    if(POI.getID() == 0):
        return

    print POI.getID()

    # don't wanna go into a wall, buddy (you right)
    if(POI.getNext() == 0):
        return

    # follow the next POI in the path
    followPath(POI.getNext())



def fireAlarm(POI, visited):
    print "Setting off alarm " + str(POI.getID())
    leftPath = setPath(POI.getLeft(), 0, POI, [], visited)
    rightPath = setPath(POI.getRight(), 0, POI, [], visited)
    middlePath = setPath(POI.getMiddle(), 0, POI, [], visited)

    print "Left path is: ", printPath(leftPath)#followPath(POI.getLeft())

    print "Right path is: ", printPath(rightPath) #followPath(POI.getRight())

    print "Middle path is: ", printPath(middlePath) #followPath(POI.getMiddle())

def printPath(thisPath):
    pathString = ""
    if (len(thisPath) == 0):
        return "none"
    for POI in thisPath:
        pathString += (str(POI.getType()) + str(POI.getID()) + " ")
    return pathString

def findPathLength(thisPath):
    if(thisPath == oo):
        pathLength = oo
    else:
        pathLength = len(thisPath)
    return pathLength


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
    allPOIs[1].setAll(wall,  allPOIs[2], wall)
    allPOIs[2].setAll(allPOIs[1], allPOIs[3], wall)
    allPOIs[3].setAll(allPOIs[2], allPOIs[4], wall)
    allPOIs[4].setAll(allPOIs[3], allPOIs[5], wall)
    allPOIs[5].setAll(wall, allPOIs[7], wall)

    for POI in allPOIs:
        visited += [False]

    fireAlarm(allPOIs[4], visited)




if __name__ == "__main__":
    main()
