from PointOfInterest import *
from path import *


def set_poi(my_poi, vis, num_alarm, num_exit):

    # set up POI as wall
    my_poi += [PointOfInterest(0, "wall")]

    # Set up five POIs as type alarm
    for i in range(1, num_alarm + 1):
        temp_poi = PointOfInterest(i, "alarm")
        my_poi += [temp_poi]

    # Set up 2 POIs as type exit
    for i in range(num_alarm + 1, num_alarm + num_exit + 1):
        my_poi += [PointOfInterest(i, "exit")]

    for poi in my_poi:
        vis += [False]


def test_case0():
    # This test case is what was used to develop path.py,
    # isn't actually anything because some alarms don't point back to
    # adjacent alarms

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 2)
    wall = all_pois[0]

    # initialize the connections from one alarm to another
    all_pois[1].set_all(wall, all_pois[7], wall)
    all_pois[2].set_all(wall, wall, wall)
    all_pois[3].set_all(wall, all_pois[1], wall)
    all_pois[4].set_all(wall, all_pois[5], all_pois[3])
    all_pois[5].set_all(wall, all_pois[6], wall)

    fire_alarm(all_pois[4], visited)


def test_case1():
    # 5 alarms, Straight line, exit on either side, middle alarm (3) detects fire
    # From Fig. 46 (p. 116) in "SMART Alarm System SD1 Documentation.pdf"

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 2)
    wall = all_pois[0]

    # initialize the connections from one alarm to another
    all_pois[1].set_all(all_pois[6], all_pois[2], wall)
    all_pois[2].set_all(all_pois[1], all_pois[3], wall)
    all_pois[3].set_all(all_pois[2], all_pois[4], wall)
    all_pois[4].set_all(all_pois[3], all_pois[5], wall)
    all_pois[5].set_all(all_pois[4], all_pois[7], wall)

    fire_alarm(all_pois[3], visited)


def test_case2():
    # 5 alarms, Straight line, exit on either side, far left alarm (1) detects fire
    # From Fig. 47 (p. 117) in "SMART Alarm System SD1 Documentation.pdf"

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 2)
    wall = all_pois[0]

    # initialize the connections from one alarm to another
    all_pois[1].set_all(all_pois[6], all_pois[2], wall)
    all_pois[2].set_all(all_pois[1], all_pois[3], wall)
    all_pois[3].set_all(all_pois[2], all_pois[4], wall)
    all_pois[4].set_all(all_pois[3], all_pois[5], wall)
    all_pois[5].set_all(all_pois[4], all_pois[7], wall)

    fire_alarm(all_pois[1], visited)


def test_case3():
    # 5 alarms, Right Elbow, exit on either side, top alarm (1) detects fire
    # From Fig. 48 (p. 117) in "SMART Alarm System SD1 Documentation.pdf

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 2)
    wall = all_pois[0]

    # initialize the connections from one alarm to another
    all_pois[1].set_all(all_pois[2], all_pois[6], wall)
    all_pois[2].set_all(all_pois[3], all_pois[1], wall)
    all_pois[3].set_all(wall, all_pois[2], all_pois[4])
    all_pois[4].set_all(all_pois[3], all_pois[5], wall)
    all_pois[5].set_all(all_pois[4], all_pois[7], wall)

    fire_alarm(all_pois[1], visited)


def test_case4():
    # 5 alarms, Right Elbow, exit on either side, corner alarm (3) detects fire
    # From Fig. 49 (p. 118) in "SMART Alarm System SD1 Documentation.pdf

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 2)
    wall = all_pois[0]

    # initialize the connections from one alarm to another
    all_pois[1].set_all(all_pois[2], all_pois[6], wall)
    all_pois[2].set_all(all_pois[3], all_pois[1], wall)
    all_pois[3].set_all(wall, all_pois[2], all_pois[4])
    all_pois[4].set_all(all_pois[3], all_pois[5], wall)
    all_pois[5].set_all(all_pois[4], all_pois[7], wall)

    fire_alarm(all_pois[3], visited)


def test_case5():
    # 5 alarms, T-Shape, 3 exits on each end, top right alarm (1) detects fire
    # From Fig. 50 (p. 119) in "SMART Alarm System SD1 Documentation.pdf

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 3)
    wall = all_pois[0]

    # initialize the connections from one alarm to another
    all_pois[1].set_all(all_pois[6], all_pois[2], wall)
    all_pois[2].set_all(all_pois[1], all_pois[3], all_pois[4])
    all_pois[3].set_all(all_pois[2], all_pois[7], wall)
    all_pois[4].set_all(all_pois[5], all_pois[2], wall)
    all_pois[5].set_all(all_pois[8], all_pois[4], wall)

    fire_alarm(all_pois[1], visited)


def test_case6():
    # 5 alarms, T-Shape, 3 exits on each end, intersection alarm (2) detects fire
    # From Fig. 51 (p. 120) in "SMART Alarm System SD1 Documentation.pdf

    all_pois = []  # list containing every POI in system
    visited = []  # a boolean value corresponding to each POI and it's ID

    set_poi(all_pois, visited, 5, 3)
    wall = all_pois[0]

    # initialize the connections from one alarm to another
    all_pois[1].set_all(all_pois[6], all_pois[2], wall)
    all_pois[2].set_all(all_pois[1], all_pois[3], all_pois[4])
    all_pois[3].set_all(all_pois[2], all_pois[7], wall)
    all_pois[4].set_all(all_pois[5], all_pois[2], wall)
    all_pois[5].set_all(all_pois[8], all_pois[4], wall)

    fire_alarm(all_pois[2], visited)
