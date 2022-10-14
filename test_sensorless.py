from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search
# You write this:

test_maze3 = Maze("maze2.maz")
test_problem = SensorlessProblem(test_maze3)
# print(test_problem.start_state)
# print(test_problem.get_successors(test_problem.start_state))

# regular heuristic
# result = astar_search(test_problem, test_problem.number_of_beliefs)
# print(result)
# test_problem.animate_path(result.path)