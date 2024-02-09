from treelib import Tree
import queue

h = {
    'S':7,
    'B':0,
    'A':3,
    'G':0
}
graph = {
    'S': {('A',2), ('B',4)},
    'A': {('S',2), ('B',1)},
    'B': {('S',4), ('A',1), ('G',4)},
    'G': {('B',4)},
}

def astar(graph, initial_node, goal_test, heuristics, is_tree, is_update):
    tree = Tree()
    priorityQueue = queue.PriorityQueue()

    priorityQueue.put((0, (initial_node, [initial_node])))
    tree.create_node(initial_node, initial_node)
    if not is_tree:
        visited = set()

    path = []

    while not priorityQueue.empty():
        cost, (current_node, node_path) = priorityQueue.get()
        cost -= heuristics[current_node]

        if not is_tree:
            if current_node in visited:
                continue
            else:
                visited.add(current_node)

        if goal_test(current_node):
            path = node_path
            break

        for neighbour, weight in graph[current_node]:
            f_n = cost + weight + heuristics[neighbour]
            priorityQueue.put((f_n, (neighbour, node_path + [neighbour])))
            if neighbour not in tree.nodes:
                tree.create_node(neighbour, neighbour, parent=current_node, data=f_n)

    tree.save2file('astar.txt', line_type='ascii')

    return ''.join(path)

# You might get a different trace due to popping different nodes.

print("=====")
print("Tree")
print("=====")
print(p:=astar(graph, 'S', lambda n: n=='G', h, is_tree=True, is_update=False))
assert(p=="SABG")

print("=====")
print("Graph")
print("=====")
print(p:=astar(graph, 'S', lambda n: n=='G', h, is_tree=False, is_update=False))
assert(p=="SBG")
