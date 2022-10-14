from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

test_maze2 = Maze("maze2.maz")
test_maze3 = Maze("maze3.maz")
test_maze4 = Maze("maze4.maz")
test_maze5 = Maze("maze5.maz")
test_maze6 = Maze("maze6.maz")
test_maze8 = Maze("maze8.maz")

# 3x4 maze
test_problem = SensorlessProblem(test_maze2)
print(test_problem.start_state)
print(test_problem.get_successors(test_problem.start_state))
result = astar_search(test_problem, test_problem.number_of_beliefs)
print(result)

# 5x6 maze
test_problem = SensorlessProblem(test_maze3)
result = astar_search(test_problem, test_problem.number_of_beliefs)
print(result)

# 9x6 maze
test_problem = SensorlessProblem(test_maze4)
result = astar_search(test_problem, test_problem.number_of_beliefs)
print(result)

# disconnected floor maze
test_problem = SensorlessProblem(test_maze5)
result = astar_search(test_problem, test_problem.number_of_beliefs)
print(result)

# thin corridor maze
test_problem = SensorlessProblem(test_maze6)
result = astar_search(test_problem, test_problem.number_of_beliefs)
print(result)

# 18x6 maze: very large but easy maze
test_problem = SensorlessProblem(test_maze8)
result = astar_search(test_problem, test_problem.number_of_beliefs)
print(result)
test_problem.animate_path(result.path)
