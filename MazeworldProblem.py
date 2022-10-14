from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze

        state = [0]
        for loc in self.maze.robotloc:
            state.append(loc)
        self.start_state = tuple(state)

        self.goal_locations = goal_locations

        # total number of robots
        self.robotsNum = len(self.maze.robotloc)//2


    def __str__(self):
        string =  "Mazeworld problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)


    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))

    # checks if there is ANOTHER robot at (x,y) and returns True if there is
    # Returns false if the robot on the floor is the one being moved
    def is_robot(self, x, y, state):
        curr_robot = state[0]
        locations = state[1:]

        for i in range(0, len(locations), 2):
            # if we are looking at location of robot to move, go on to next location
            if i == 2*curr_robot:
                continue

            rx = locations[i]
            ry = locations[i + 1]
            if rx == x and ry == y:
                return True

        return False

    # gets the children of the current state
    def get_successors(self, state):
        children = []

        robot = state[0]                            # first value of state gives robot to move
        index = (2*robot) + 1                       # the index of the robot's x location in the state
        location = state[index: index+2]            # the location of the robot to move
        
        # setting up the value of the next robot to be moved
        if robot == self.robotsNum - 1:
            next_robot = 0
        else:
            next_robot = robot + 1

        # possible moves: N, E, W, S, stay put
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]
        
        for move in moves:
            x_loc = location[0] + move[0]
            y_loc = location[1] + move[1]
            
            # check if child is legal move
            # it is legal if the location is a floor that does not have another robot
            if self.maze.is_floor(x_loc, y_loc):

                # if the potential location has a robot, but the robot is itself (staying put), add the child
                if not (self.is_robot(x_loc, y_loc, state)):
                    # getting the state as is
                    child = list(state)
                    # adding the next robot value to it
                    child[0] = next_robot
                    # changing only the location for the robot being moved
                    child[index] = x_loc
                    child[index+1] = y_loc

                    children.append(tuple(child))   
                
        return children
    
    # checks if the current state is the goal
    def goal_test(self, state):
        # removing the value for the robot turn to get the locations of the robots only
        locations =  state[1:]
        return locations == self.goal_locations


    def cost_fn(self, parent_state, child_state, visited):
        # if child state has the robot moving
        # only then does it use up 1 unit of fuel
        
        # the robot who will be moving
        robot = parent_state[0]

        # the robot did not stay put
        if child_state[1:] != parent_state[1:]:
            return visited[parent_state] + 1
        
        # otherwise it did not move
        return visited[parent_state]


    # uses manhattan distance for the heuristic
    def manhattan_heuristic(self, state):
        # the total distance from the goal state
        robot = state[0]
        locations = state[1:]
        # start the loop from after the value for robot turn
        # going through the locations of each robot

        i = 2*robot
        x = locations[i]
        y = locations[i+1]

        # the goal coordinates for the robot
        goal_x = self.goal_locations[i]
        goal_y = self.goal_locations[i+1]

        # the manhattan distances from the goal location to the moving robot
        return abs(goal_x - x) + abs(goal_y - y)

## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 1, 2, 1)))
