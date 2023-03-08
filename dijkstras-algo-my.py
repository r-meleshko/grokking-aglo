def dijkstra(graph, start, end):

    path_graph = {i: ['', float('inf')] for i in list(graph.keys()) + [end]}
    path_graph[start][1] = 0

    while graph:
        left_nodes = {i: path_graph[i] for i in path_graph if i in graph.keys()}  # select unprocessed nodes
        node = sorted(left_nodes.items(), key=lambda x: x[1][1])[0][0]  # get the lowest cost node
        node_dist = path_graph[node][1]  # distance to get to the node
        for neighbour, dist in graph[node]:  # update neighbours distance if lower than actual
            if node_dist + dist < path_graph[neighbour][1]:
                path_graph[neighbour] = [node, node_dist + dist]
        graph.pop(node)  # remove node from the list of nodes to check

    path = []
    parent = path_graph[end][0]
    while parent != '':
        path = path + [parent]
        parent = path_graph[parent][0]
    print(path[::-1])


graph = dict()
graph['book'] = [['lp', 5], ['poster', 0]]
graph['lp'] = [['bass', 15], ['drum', 20]]
graph['poster'] = [['bass', 30], ['drum', 35]]
graph['drum'] = [['piano', 10]]
graph['bass'] = [['piano', 20]]
dijkstra(graph, 'book', 'piano')


graph = dict()
graph['start'] = [['A', 5], ['D', 2]]
graph['A'] = [['B', 4], ['E', 2]]
graph['B'] = [['C', 3], ['E', 6]]
graph['D'] = [['A', 8], ['E', 7]]
graph['E'] = [['C', 1]]
dijkstra(graph, 'start', 'C')


graph = dict()
graph['start'] = [['A', 10]]
graph['A'] = [['B', 20]]
graph['B'] = [['D', 1], ['C', 30]]
graph['D'] = [['A', 1]]

dijkstra(graph, 'start', 'C')
