from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze1 = Maze("maze1.maz")
test_maze2 = Maze("maze2.maz")
test_maze3 = Maze("maze3.maz")
test_maze4 = Maze("maze4.maz")
test_maze5 = Maze("maze5.maz")
test_maze6 = Maze("maze6.maz")
test_maze7 = Maze("maze7.maz")


test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
# result = astar_search(test_mp, null_heuristic)
# print(result)

# # this should do a bit better:
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)

# testing successor method
# test_mp = MazeworldProblem(test_maze3, (1, 0, 1, 1, 2, 1))
# print(test_mp.get_successors((1, 1, 0, 1, 1, 2, 1)))
# print(test_mp.get_successors((2, 1, 0, 1, 2, 2, 1)))

# # testing on different, further goal state
# test_mp = MazeworldProblem(test_maze3, (2, 4, 2, 5, 3, 4))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# # testing on map with no robots
# test_mp = MazeworldProblem(test_maze1, ((2, 1, 0, 1, 2, 2, 1)))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)

# # testing on 1 robot map
# test_mp = MazeworldProblem(test_maze2, ((2, 2)))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# my mazes

# 9x6 maze: a maze that has a zigzag pattern, messing with the manhattan heuristic
test_mp = MazeworldProblem(test_maze4, (7, 1, 7, 2, 7, 4))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)

# 9x6 maze: a maze that has disconnected floors, shouldn't reach
test_mp = MazeworldProblem(test_maze5, (7, 1, 7, 2, 7, 4))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)

# easy thin corridor maze
test_mp = MazeworldProblem(test_maze6, (1, 4, 1, 3, 1, 2))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)

# very thin corridor maze, with only one floor cell to reverse order: very cool!!
test_mp = MazeworldProblem(test_maze7, (1, 0, 1, 1, 1, 2))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)