from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.cost = transition_cost

    def priority(self):
        # you write this part
        return self.heuristic + self.cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()

    # method for checking if a state already exists in the heap
    def __eq__(self, other):
        return self.state == other.state

# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)    # heappsh(heap, item), so pqueue is heap

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    # state key, cost item
    visited_cost = {}
    visited_cost[start_node.state] = 0

    # you write the rest:
    while pqueue:
        # if the heap is not empty, pop the smallest element
        curr_node = heappop(pqueue)
        curr_state = curr_node.state

        if search_problem.goal_test(curr_state):
            solution.path = backchain(curr_node)
            return solution
        
        for child in search_problem.get_successors(curr_state):
            child_cost = search_problem.cost_fn(curr_state, child, visited_cost)
            child_node = AstarNode(child, heuristic_fn(child), curr_node,  child_cost)

            # if we have not visited this child before, or we found a child with lower cost
            if child not in visited_cost or child_cost < visited_cost[child]:
                # add to visited set or replace the existing higher cost node
                visited_cost[child] = child_cost
                heappush(pqueue, child_node)
                
            elif child_cost < visited_cost[child]:
                visited_cost[child] = child_cost
                heappush(pqueue, child_node)
    
    return solution

