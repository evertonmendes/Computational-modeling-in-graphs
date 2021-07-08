from math import inf

graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}


def dijkstra(graph,start,goal):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph.copy()
    infinity = inf
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    # Determine which is minimum node. What does that mean?
    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for edge, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[edge]:
                shortest_distance[edge] = weight + shortest_distance[minNode]
                predecessor[edge] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if shortest_distance[goal] != infinity:
        print(str(shortest_distance[goal]))
        print('And the path is ' + str(path))


#dijkstra(graph, 'c', 'e')