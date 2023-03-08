def dijkstra(stucture, start, end):
    graph = dict()
    for node, neighbours in structure:
        graph[node] = {}
        for neighbour in neighbours:
            graph[node][neighbour[0]] = neighbour[1]

    parents = {i: None for i in graph}
    costs = {i: float('inf') for i in graph}

    for neighbour in graph[start]:
        costs[neighbour] = graph[start][neighbour]
        parents[neighbour] = start

    processed = [start]

    def find_lowest_cost_node(costs, processed):
        filtered_costs = {i: costs[i] for i in costs if
                          i not in processed}  # select only nodes that werere not toched before
        try:
            return sorted(filtered_costs.items(), key=lambda x: x[1])[0][0]
        except IndexError:
            return None

    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours:
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    path = []
    parent = parents[end]
    while parent:
        path = path + [parent]
        parent = parents[parent]
    print(path[::-1])


structure = [('book', [['lp', 5], ['poster', 0]]),
             ('lp', [['bass', 15], ['drum', 20]]),
             ('poster', [['bass', 30], ['drum', 35]]),
             ('drum', [['piano', 10]]),
             ('bass', [['piano', 20]]),
             ('piano', [])]
dijkstra(structure, 'book', 'piano')


structure = [('start', [['A', 5], ['D', 2]]),
             ('A', [['B', 4], ['E', 2]]),
             ('B', [['C', 3], ['E', 6]]),
             ('D', [['A', 8], ['E', 7]]),
             ('E', [['C', 1]]),
             ('C', [])]
dijkstra(structure, 'start', 'C')


structure = [('start', [['A', 10]]),
             ('A', [['B', 20]]),
             ('B', [['D', 1], ['C', 30]]),
             ('D', [['A', 1]]),
             ('C', [])]
dijkstra(structure, 'start', 'C')