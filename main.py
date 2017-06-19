import path

oo = 1e9

# this is the algorithm code for the alarm hub

class Alarm:
    # constructor of an alarm
    def __init__(self, id):
        self.id = id
        self.left = 0
        self.leftDistance = oo
        self.right = 0
        self.rightDistance = oo
        self.middle = 0
        self.middleDistance = oo
        self.leftLED = 0
        self.rightLED = 0
        self.middleLED = 0
        self.buzzer = 0
        self.nextAlarm = 0
        self.nearestAlarms = []

    # setters for alarms
    def setLeft(self, alarm, distance):
        self.left = alarm
        self.leftDistance = distance

    def setRight(self, alarm, distance):
        self.right = alarm
        self.rightDistance = distance

    def setMiddle(self, alarm, distance):
        self.middle = alarm
        self.middleDistance = distance


    def setAll(self, left, right, middle, distL, distR, distM):
        self.setLeft(left, distL)
        self.setRight(right, distR)
        self.setMiddle(middle, distM)
        self.nearestAlarms = [left, right, middle]

    def setNext(self, alarm):
        self.nextAlarm = alarm

    # getters for alarms
    def getLeft(self):
        return self.left

    def getLeftDistance(self):
        return self.leftDistance

    def getRight(self):
        return self.right

    def getRightDistance(self):
        return self.rightDistance

    def getMiddle(self):
        return self.middle

    def getMiddleDistance(self):
        return self.middleDistance

    def getID(self):
        return self.id

    def getNext(self):
        return self.nextAlarm

    def getNearestAlarms(self):
        return self.nearestAlarms

    # Returns the distance between the current alarm and an other alarm,
    # if it's adjacent, we should consider expanding this to any alarm
    def getDistance(self, otherAlarm):
        alarms = self.getNearestAlarms()
        if otherAlarm == alarms[0]:
            return self.getLeftDistance()
        elif otherAlarm == alarms[1]:
            return self.getRightDistance()
        elif otherAlarm == alarms[2]:
            return self.getMiddleDistance()
        else:
            print 'The alarm is not adjacent to the current alarm'
            return



def setPath(alarm, length, alarmFrom):


    if(alarm == 0) or (alarm.getID() == 0):
        return 1000


    if(alarm.getID() == "exit"):
        return length+1

    # base case
    if (alarm.getLeft() != 0) and (alarm.getLeft().getID() == "exit"):
        alarm.setNext(alarm.getLeft())
        return length + 1
    elif (alarm.getRight() != 0) and (alarm.getRight().getID() == "exit"):
        alarm.setNext(alarm.getRight())
        return length + 1
    elif (alarm.getMiddle() != 0) and (alarm.getMiddle().getID() == "exit"):
        alarm.setNext(alarm.getMiddle())
        return length + 1

    # set the path lengths for the left direction
    # we do not want to go back the way we came so we have a check for that.
    if(alarm.getLeft() != 0 and alarmFrom.getID() != alarm.getLeft().getID()):
         leftPath = setPath(alarm.getLeft(), length, alarm) + 1
    else:
        leftPath = 1000


    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(alarm.getRight() != 0 and alarmFrom.getID() != alarm.getRight().getID()):
        rightPath = setPath(alarm.getRight(), length, alarm) + 1
    else:
        rightPath = 1000

    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(alarm.getMiddle() != 0 and alarmFrom.getID() != alarm.getMiddle().getID()):
        middlePath = setPath(alarm.getMiddle(), length, alarm) + 1
    else:
        middlePath = 1000;


    #find the minimum path, and set the next alarm
    if((leftPath < rightPath) and (leftPath < middlePath)):
        alarm.setNext(alarm.getLeft())
        return leftPath
    elif((rightPath < leftPath) and (rightPath < middlePath)):
        alarm.setNext(alarm.getRight())
        return rightPath
    elif((middlePath < leftPath) and (middlePath < rightPath)):
        alarm.setNext(alarm.getMiddle())
        return middlePath
    ## if the paths are equal go left cause why not
    elif(rightPath == leftPath and alarmFrom.getID() != alarmFrom.getLeft().getID()):
        alarm.setNext(alarm.getLeft())
        return leftPath
    else:
        alarm.setNext(alarm.getMiddle())
        return middlePath


# follows a path until it gets to a wall or exit, we
# need to create a path class, to pass the previously
# visited alarms, and measure length
def followPath(alarm):

    if (alarm == 0):
        return

    if(alarm.getID() == 0):
        return

    print alarm.getID()

    # don't wanna go into a wall, buddy (you right)
    if(alarm.getNext() == 0):
        return

    # follow the next alarm in the path
    followPath(alarm.getNext())


#def followPath(alarm, length):

    #if alarm == 0:
    #    return

    #if alarm.getID() == 0:
    #    return

    #if alarm.getID() == "exit":
    #    return



def fireAlarm(alarm):
    print "Setting off alarm " + str(alarm.getID())
    setPath(alarm.getLeft(), 0, alarm)
    setPath(alarm.getRight(), 0, alarm)
    setPath(alarm.getMiddle(), 0, alarm)

    print "Left path is: ", followPath(alarm.getLeft())
    print "It's distance is:\n"

    print "Right path is: ", followPath(alarm.getRight())
    print "It's distance is:\n"

    print "Middle path is: ", followPath(alarm.getMiddle())
    print "It's distance is:\n"


# main function
def main():
    # Set up five alarms
    alarm1 = Alarm(1)
    alarm2 = Alarm(2)
    alarm3 = Alarm(3)
    alarm4 = Alarm(4)
    alarm5 = Alarm(5)

    # Set up 3 exits
    exit1 = Alarm("exit")
    exit2 = Alarm("exit")
    exit3 = Alarm("exit")

    # initialize the connections from one alarm to another
    alarm1.setAll(exit1, alarm2, 0, 4, 3, oo)
    alarm2.setAll(alarm1, alarm5, alarm3, 3, 6, 4)
    alarm3.setAll(alarm2, alarm4, 0, 4, 2, oo)
    alarm4.setAll(alarm3, exit2, 0, 2, 3, oo)
    alarm5.setAll(alarm2, exit3, 0, 6, 2, oo)

    fireAlarm(alarm3)

    # print alarm5.getDistance(exit3)


if __name__ == "__main__":
    main()
