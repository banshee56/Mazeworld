from Maze import Maze
from time import sleep

class SensorlessProblem:
    def __init__(self, maze):
        self.maze = maze

        start_state = []
        # gathering the starting locations for the initial belief state
        width = 0
        height = self.maze.height - 1
        for i in range(len(self.maze.map)):
            char = self.maze.map[i]
            
            # if '.', that's an open floor and possible location
            if char == '.':
                possible_location = (width, height)
                start_state.append(possible_location)

            # resetting width and going down the maze
            if width == self.maze.width - 1:
                width = 0
                height -= 1
            else:
                width += 1

        self.start_state = tuple(start_state)
            


    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def get_successors(self, state):
        # can move N, E, W, S 
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        children = []

        for move in moves:
            child = set()

            for loc in state:
                # trying to move the robot
                x_loc = loc[0] + move[0]
                y_loc = loc[1] + move[1]

                # if out of maze or on an obstacle, we hit a wall, so robot stays put, add current loc to children state
                if not self.maze.is_floor(x_loc, y_loc):
                    child.add((loc[0], loc[1]))

                # if it is on a floor, it moved to a different spot, so add this to the children state
                elif self.maze.is_floor(x_loc, y_loc):
                    child.add((x_loc, y_loc))
            
            children.append(tuple(child))
        return tuple(children)
    
    # prof said all costs can be 1/the same
    def cost_fn(self, parent, state, visited):
        return visited[parent] + 1

    # len of the number of possible states in the belief states
    def number_of_beliefs(self, state):
        return len(state)

    # just a singleton remains in the belief state
    def goal_test(self, state):
        return len(state) == 1

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            locs = []
            for loc in state:
                locs.append(loc[0])
                locs.append(loc[1])

            print(str(self))
            self.maze.robotloc = tuple(locs)
            sleep(3)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze2.maz")
    test_problem = SensorlessProblem(test_maze3)
    print(test_problem.start_state)
    print(test_problem.get_successors(test_problem.start_state))
