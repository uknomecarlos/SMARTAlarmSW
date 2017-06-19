# class file for "path" for alarm hub

class Path:
    # constructor of a path
    def __init__(self, id):
        self.id = id
        self.length = 0
        self.alarmsInPath = []
        self.lastAlarm = getLastAlarm()

    # setters for paths
    def setLength(self, prevPath, newAlarm):
        self.length = prevPath.getLength() + newAlarm.getDistance(self.getLastAlarm())

    def getLastAlarm(self):
        length = self.alarmsInPath.__len__()
        return self.alarmsInPath[length - 1]

    def getLength(self):
        return self.length