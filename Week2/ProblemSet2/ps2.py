# 6.00.2x Problem Set 2: Simulating robots

import math
import random
import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    
    # Generates a field with a width of "width" and height of "height"

    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.clean = []

    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = math.floor(pos.x)
        y = math.floor(pos.y)
        clean_tile = (x, y)
        
        self.clean.append(clean_tile)
        return self.clean


    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.
        
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """

        x = math.floor(m)
        y = math.floor(n)
        tile = (x, y)

        if tile in self.clean:
            return True
        else: 
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

        

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.clean)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        random_x = random.random() + random.choice(range(0, self.width))
        random_y = random.random() + random.choice(range(0, self.height))

        return Position(random_x, random_y)


    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        
        x = math.floor(pos.x)
        y = math.floor(pos.y)

        if x in range(0, self.width):
            if y in range(0, self.height):
                return True
            else: 
                return False
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        
        self.room = room
        self.speed = speed
        self.pos = room.getRandomPosition()
        self.x = self.pos.x
        self.y = self.pos.y
        room.clean.append((int(self.x), int(self.y)))
        self.direction = random.choice(range(0, 360, 1))

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return Position(self.x, self.y)
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """

        return self.direction
        
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """

        self.pos = position
        self.x = position.x
        self.y = position.y
        return self.pos

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        return self.direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        # make temporary position object
        temp_position_object = Position(self.x, self.y)
        # # make new position
        temp_position = temp_position_object.getNewPosition(self.direction, self.speed)
        # # print temp_position


        while not self.room.isPositionInRoom(temp_position):
            # if change is not valid, keep position and change direction
            self.setRobotDirection(random.choice(range(0, 360, 1)))
            temp_position = temp_position_object.getNewPosition(self.direction, self.speed)
        
    	# if the change is valid, change robot's position. 
     	self.setRobotPosition(temp_position)
     	# mark as cleaned 
     	if not self.room.isTileCleaned(self.x, self.y):
     		self.room.cleanTileAtPosition(self.pos)
        

        

        

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        
        # create temp position
        temp_position = self.pos.getNewPosition(random.choice(range(0, 360, 1)), self.speed)

        while not self.room.isPositionInRoom(temp_position):
            temp_position = self.pos.getNewPosition(random.choice(range(0, 360, 1)), self.speed)

        # if the change is valid, change robot's position. 
        self.setRobotPosition(temp_position)
        # mark as cleaned 
        if not self.room.isTileCleaned(self.x, self.y):
            self.room.cleanTileAtPosition(self.pos) 


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """

    # animation
    # anim = ps2_visualize.RobotVisualization(num_robots, width, height)

    results = []
    

    for i in range(num_trials):
        
        # assign number of times, a robot and a new (dirty) room
        robots = []
        dirty_room = RectangularRoom(width, height)

        for n in range(num_robots):
            robot = robot_type(dirty_room, speed)
            robots.append(robot)

        counter = 0
        roomCoverage = float(robot.room.getNumCleanedTiles()) / robot.room.getNumTiles()
        

        # conduct cleaning experiment
        while roomCoverage < min_coverage:
            for robot in robots:
                # anim.update(dirty_room, robots)
                robot.updatePositionAndClean()
                
            counter+=1
            roomCoverage = float(robot.room.getNumCleanedTiles()) / robot.room.getNumTiles()
        
        results.append(counter)

    # anim.done()
    average = sum(results)/len(results)
    return average

    
    

# Uncomment this line to see how much your simulation takes on average
print runSimulation(4, 1.0, 10, 10, 0.9, 3, RandomWalkRobot)


# === Problem 4




def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()



    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.

# showPlot1("Average cleaning time per robot", "number of robots", "Required time")

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

showPlot2("Average time it takes to clean a room of certain width and hight", "aspect_ratios", "time-steps")
