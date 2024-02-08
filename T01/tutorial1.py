graph = {
    'S': {('A', 1), ('B', 5),  ('C', 15)},
    'A': {('G', 10), ('S', 1)},
    'B': {('G', 5), ('S', 5)},
    'C': {('G', 5), ('S', 15)},
    'G': set()
}

from priority_queue import PriorityQueue
from collections import defaultdict

# Return the path found
def uniform_cost_search(graph, inital_node, goal_test, is_tree, is_update):

    frontier = PriorityQueue('min')
    frontier.append((inital_node, ""), 0)

    if is_tree:
        while frontier.__len__ != 0:
            node = frontier.pop()

            if goal_test(node[1][0]):
                return node[1][1] + str(node[1][0])

            for neighbour in graph[node[1][0]]:
                key, priority = neighbour
                frontier.append((key, node[1][1] + str(node[1][0])), priority + node[0])
    else:
        visited = set()
        while frontier.__len__ != 0:
            node = frontier.pop()

            if node[1][0] in visited:
                continue
            visited.add(node[1][0])

            if goal_test(node[1][0]):
                return node[1][1] + str(node[1][0])

            for neighbour in graph[node[1][0]]:
                key, priority = neighbour
                frontier.append((key, node[1][1] + str(node[1][0])), priority + node[0])

print("=====")
print("Tree")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=True, is_update=False))
assert(p=="SBG")

print("=====")
print("Graph")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=False, is_update=True))
assert(p=="SBG")