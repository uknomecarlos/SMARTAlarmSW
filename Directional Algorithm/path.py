# SMART Alarm System
# Authors: Carlos Castro & Lucas Plager
# University of Central Florida
# path.py
# Path Finding algorithm for the SMART Alarm hub
# Function: Read configuration of alarms in a building and return fastest
# exit path for each alarm, and shortest path from fire

# Global Variables:
oo = 1e9  # "infinity"


def set_path(poi_from, poi, this_path, visited):
    # This function finds the shortest path from the POI value passed
    # poi_from is the previous POI in the path, poi is the current POI,
    # this_path is a list that holds the POI in the path, and visited
    # is a boolean list for checking if a POI has been visited
    # Return value: a boolean list "visited"

    # Check if POI is a wall
    if(poi.get_type() == "wall") or (poi.get_id() == 0):
        return visited

    # Mark current POI as visited
    visited[poi.get_id()] = True

    # Check if POI is an exit
    if poi.get_type() == "exit":
        return visited

    # base case
    # Check each adjacent POI, if it's not a wall, AND it's an exit, set the adjacent
    # POI as next and mark as visited since the end of the path has been reached, return
    if (poi.get_left().get_type() != "wall") and (poi.get_left().get_type() == "exit"):
        poi.set_next(poi.get_left())
        visited[poi.get_left().get_id()] = True
        return visited
    elif (poi.get_right().get_type() != "wall") and (poi.get_right().get_type() == "exit"):
        poi.set_next(poi.get_right())
        visited[poi.get_right().get_id()] = True
        return visited
    elif (poi.get_middle().get_type() != "wall") and (poi.get_middle().get_type() == "exit"):
        poi.set_next(poi.get_middle())
        visited[poi.get_middle().get_id()] = True
        return visited

    # set the path for the left direction
    # we do not want to go back the way we came so we have a check for that.
    if (poi.get_left().get_type() != "wall") and not(visited[poi.get_left().get_id()]):
        left_vis = set_path(poi, poi.get_left(), this_path, visited)
    else:
        left_vis = oo

    # set the path for the right direction
    # we do not want to go back the way we came so we have a check for that.
    if (poi.get_right().get_type() != "wall") and not(visited[poi.get_right().get_id()]):
        right_vis = set_path(poi, poi.get_right(), this_path, visited)
    else:
        right_vis = oo

    # set the path for the middle
    # we do not want to go back the way we came so we have a check for that.
    if (poi.get_middle().get_type() != "wall") and not(visited[poi.get_middle().get_id()]):
        middle_vis = set_path(poi, poi.get_middle(), this_path, visited)
    else:
        middle_vis = oo

    # Follow the shortest path in each direction from the current POI
    left_path = []
    follow_path(poi.get_left(), left_path, left_vis)
    middle_path = []
    follow_path(poi.get_middle(), middle_path, middle_vis)
    right_path = []
    follow_path(poi.get_right(), right_path, right_vis)

    # Find length for each path from the current POI
    left_length = find_path_length(left_path)
    right_length = find_path_length(right_path)
    middle_length = find_path_length(middle_path)

    # find the minimum path, and set the next POI for the current POI to follow it's shortest path
    if (left_length < right_length) and (left_length < middle_length):
        poi.set_next(poi.get_left())
        visited[poi.get_left().get_id()] = True
        return visited
    elif (right_length < left_length) and (right_length < middle_length):
        poi.set_next(poi.get_right())
        visited[poi.get_right().get_id()] = True
        return visited
    elif (middle_length < left_length) and (middle_length < right_length):
        poi.set_next(poi.get_middle())
        visited[poi.get_middle().get_id()] = True
        return visited
    # if the paths are equal go left cause why not
    elif (right_length == left_length) and (poi.get_id() != poi_from.get_left().get_id()):
        poi.set_next(poi.get_left())
        visited[poi.get_left().get_id()] = True
        return visited
    elif(right_length == middle_length) and (poi.get_id() != poi_from.get_right().get_id()):
        poi.set_next(poi.get_right())
        visited[poi.get_middle().get_id()] = True
        return visited
    elif (middle_length == left_length) and (poi.get_id() != poi_from.get_left().get_id()):
        poi.set_next(poi.get_left())
        visited[poi.get_left().get_id()] = True
        return visited
    else:
        poi.set_next(poi.get_left())
        visited[poi.get_left().get_id()] = True
        return visited


def follow_path(poi, my_path, vis):
    # follows a path until it gets to a wall or exit, creates an array of POIs in ascending order from
    # the fire to the exit, saved at the value passed in for "my_path"

    if (poi == 0) or (poi.get_type() == "wall"):
        return

    if (poi.get_id() == 0) or (vis == oo):
        return

    my_path += [poi]

    # don't wanna go into a wall, buddy (you right)
    if (poi.get_next() == 0) or (poi.get_next().get_type() == "wall"):
        return

    # follow the next POI in the path
    follow_path(poi.get_next(), my_path, vis)


def fire_alarm(poi, visited):
    # Marks the current POI as the site of the fire, finds the shortest
    # path from the fire at the current POI

    print "Setting off alarm " + str(poi.get_id())
    visited[poi.get_id()] = True

    # Find shortest path in each direction of fire
    set_path(poi, poi.get_left(), [], visited)
    set_path(poi, poi.get_middle(), [], visited)
    set_path(poi, poi.get_right(), [], visited)

    # use "follow_path" to create POI lists that contain the path in ascending order from
    # the fire to the nearest exit
    left_path = []
    follow_path(poi.get_left(), left_path, visited)
    print "left path: " + print_path(left_path)
    middle_path = []
    follow_path(poi.get_middle(), middle_path, visited)
    print "middle path: " + print_path(middle_path)
    right_path = []
    follow_path(poi.get_right(), right_path, visited)
    print "right path: " + print_path(right_path)

    left_length = find_path_length(left_path)
    middle_length = find_path_length(middle_path)
    right_length = find_path_length(right_path)

    # find the minimum path, and set the next POI
    if (left_length < right_length) and (left_length < middle_length):
        print "Shortest Path is Left Path"
    elif (right_length < left_length) and (right_length < middle_length):
        print "Shortest Path is Right Path"
    elif (middle_length < left_length) and (middle_length < right_length):
        print "Shortest Path is Middle Path"
    # if the right and left paths are equal go left cause why not,
    elif right_length == left_length:
        print "Shortest Paths are Left and Right Paths"
    elif right_length == middle_length:
        print "Shortest Paths are Middle and Right Paths"
    elif left_length == middle_length:
        print "Shortest Paths are Left and Middle Paths"
    else:
        print "Shortest Path is Left Path"


def print_path(this_path):
    # prints a path in the order from fire to exit
    path_string = ""
    if len(this_path) == 0:
        return "none"
    for poi in this_path:
        path_string += (str(poi.get_type()) + str(poi.get_id()) + " -> ")
    return path_string


def find_path_length(this_path):
    # Find the length of a given path

    if (this_path == oo) or (len(this_path) == 0):
        path_length = oo
    else:
        path_length = len(this_path)
    return path_length
