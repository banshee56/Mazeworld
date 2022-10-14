from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
# test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# test_mp = MazeworldProblem(test_maze3, (1, 0, 1, 1, 2, 1))
test_mp = MazeworldProblem(test_maze3, (2, 4, 2, 5, 3, 4))

# print(test_mp.get_successors(test_mp.start_state))
# print(test_mp.get_successors((1, 1, 0, 1, 1, 2, 1)))
# print(test_mp.get_successors((2, 1, 0, 1, 2, 2, 1)))
# [(0, 1, 0, 1, 2, 2, 2), (0, 1, 0, 1, 2, 3, 1), (0, 1, 0, 1, 2, 1, 1)]

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)


# Your additional tests here:
