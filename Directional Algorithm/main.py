import path

oo = 1e9

# this is the algorithm code for the alarm hub

class Alarm:
    # constructor of an alarm
    def __init__(self, id):
        self.id = id
        self.left = 0
        self.right = 0
        self.middle = 0
        self.leftLED = 0
        self.rightLED = 0
        self.middleLED = 0
        self.buzzer = 0
        self.nextAlarm = 0
        self.nearestAlarms = []

    # setters for alarms
    def setLeft(self, alarm):
        self.left = alarm

    def setRight(self, alarm):
        self.right = alarm

    def setMiddle(self, alarm):
        self.middle = alarm

    def setAll(self, left, right, middle):
        self.setLeft(left)
        self.setRight(right)
        self.setMiddle(middle)
        self.nearestAlarms = [left, right, middle]

    def setNext(self, alarm):
        self.nextAlarm = alarm

    # getters for alarms
    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getMiddle(self):
        return self.middle

    def getID(self):
        return self.id

    def getNext(self):
        return self.nextAlarm

    def getNearestAlarms(self):
        return self.nearestAlarms


def setPath(alarm, length, alarmFrom):


    if(alarm == 0) or (alarm.getID() == 0):
        return oo


    if(alarm.getID() == "exit"):
        return length + 1

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
        leftPath = oo


    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(alarm.getRight() != 0 and alarmFrom.getID() != alarm.getRight().getID()):
        rightPath = setPath(alarm.getRight(), length, alarm) + 1
    else:
        rightPath = oo

    # set the path lengths for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if(alarm.getMiddle() != 0 and alarmFrom.getID() != alarm.getMiddle().getID()):
        middlePath = setPath(alarm.getMiddle(), length, alarm) + 1
    else:
        middlePath = oo


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



def fireAlarm(alarm):
    print "Setting off alarm " + str(alarm.getID())
    setPath(alarm.getLeft(), 0, alarm)
    setPath(alarm.getRight(), 0, alarm)
    setPath(alarm.getMiddle(), 0, alarm)

    print "Left path is: ", followPath(alarm.getLeft())

    print "Right path is: ", followPath(alarm.getRight())

    print "Middle path is: ", followPath(alarm.getMiddle())


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
    alarm1.setAll(exit1, alarm2, 0)
    alarm2.setAll(alarm1, alarm5, alarm3)
    alarm3.setAll(alarm2, alarm4, 0)
    alarm4.setAll(alarm3, exit2, 0)
    alarm5.setAll(alarm2, exit3, 0)

    fireAlarm(alarm3)

    # print alarm5.getDistance(exit3)


if __name__ == "__main__":
    main()
