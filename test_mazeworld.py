from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
# result = astar_search(test_mp, null_heuristic)
# print(result)

# # this should do a bit better:
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)


# Your additional tests here:

# testing successor method
# test_mp = MazeworldProblem(test_maze3, (1, 0, 1, 1, 2, 1))
# print(test_mp.get_successors((1, 1, 0, 1, 1, 2, 1)))
# print(test_mp.get_successors((2, 1, 0, 1, 2, 2, 1)))

# # testing on different, further goal state
test_mp = MazeworldProblem(test_maze3, (2, 4, 2, 5, 3, 4))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# # testing on map with no robots
# test_maze1 = Maze("maze1.maz")
# test_mp = MazeworldProblem(test_maze1, ((2, 1, 0, 1, 2, 2, 1)))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)

# # testing on 1 robot map
# test_maze1 = Maze("maze2.maz")
# test_mp = MazeworldProblem(test_maze1, ((2, 2)))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)
