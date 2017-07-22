# SMART Alarm System
# Authors: Carlos Castro & Lucas Plager
# University of Central Florida
# PointOfInterest.py
# Path Finding algorithm for the SMART Alarm hub
# Function: Read configuration of alarms in a building and return fastest
# exit path for each alarm, and shortest path from fire

# Global Variables:
oo = 1e9  # "infinity"


class PointOfInterest:
    # Three types of POI: alarm, exit and wall, ID = 0 for walls, ID is
    # give to every alarm and exit. Two constructor parameters: ID and Type,
    # all other class values are initiated to 0

    # constructor
    def __init__(self, my_id, my_type):
        self.id = my_id
        self.type = my_type
        self.left = 0
        self.right = 0
        self.middle = 0
        self.leftLED = 0
        self.rightLED = 0
        self.middleLED = 0
        self.buzzer = 0
        self.nextPOI = 0

    # setters
    # sets POI to the left of the current POI
    def set_left(self, poi):
        self.left = poi

    # sets POI to the right of the current POI
    def set_right(self, poi):
        self.right = poi

    # sets POI in across from the current POI
    def set_middle(self, poi):
        self.middle = poi

    # sets the POIs in each direction of the current POI
    def set_all(self, left, middle, right):
        self.set_left(left)
        self.set_right(right)
        self.set_right(right)
        self.set_middle(middle)

    # sets the next POI to follow in a path for the given POI
    def set_next(self, poi):
        self.nextPOI = poi

    # getters
    # returns POI to the left of current POI
    def get_left(self):
        return self.left

    # returns POI to the right of the current POI
    def get_right(self):
        return self.right

    # returns POI across from the current POI
    def get_middle(self):
        return self.middle

    # returns the ID of the POI
    def get_id(self):
        return self.id

    # returns the Type of the POI
    def get_type(self):
        return self.type

    # returns the next POI to follow in a path for the current POI
    def get_next(self):
        return self.nextPOI
