from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.start_state
        self.goal_locations = goal_locations


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

    # checks if the current state is the goal
    def goal_test(self, state):
        # removing the value for the robot turn to get the locations of the robots only
        locations =  state[1:]
        return locations == self.goal_locations

    def cost_fn(self, parent, child, visited):
        # if child state has the robot moving
        # only then does it use up 1 unit of fuel
        
        # the robot who will be moving
        robot = parent[0]

        # the robot moved
        if child[robot+1] != parent[robot+1]:
            return visited[parent] + 1
        
        # otherwise it did not move
        return visited[parent]

    def heuristic_fn(self, state):
        # state (R, xa, ya, xb, yb, xc, yc)
        d = 0

        for i in range(1, len(state), 2):
            x = state[i]
            y = state[i+1]

            goal_x = self.goal_locations[i-1]
            goal_y = self.goal_locations[i]

            d += abs(goal_x - x) + abs(goal_y - y)

        return d

## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
