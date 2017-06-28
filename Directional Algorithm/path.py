# class file for "path" for alarm hub

oo = 1e9

class Path:
    # constructor of a path
    def __init__(self, id, originAlarm):
        self.id = id
        self.origin = originAlarm
        self.alarmsInPath = [originAlarm]
        self.length = len(self.alarmsInPath) - 1
        self.lastAlarm = getLastAlarm()


    # getters for paths
    def getLastAlarm(self):
        return self.alarmsInPath[self.length]

    def getPathAlarms(self):
        return self.alarmsInPath

    def getPathOrigin(self):
        return self.origin

    def getLength(self):
        return self.length

    def addAlarm(self, newAlarm):
        self.alarmsInPath.append(newAlarm)
        self.length += 1

def addToPath(path, newAlarm):
    path.addAlarm(newAlarm)

   # def returnPath(self):

# follows a path until it gets to a wall or exit,
# employs use of path class unlike previous iteration (found in main.py)
def followPath(path, index):
    # type: (Path, Integer) -> nothing

    thisAlarm = path.getPathAlarms()[index]

    if(index == path.getLength() or thisAlarm == 0 or thisAlarm.getID() == 0):
        return

    print thisAlarm.getID()

    # follow the next alarm in the path
    followPath(path, index + 1)

# setPath helper function
def setPath(alarm):
    path = Path(alarm.getID(), alarm)
    #path = setPath(path, 0)
    return path
