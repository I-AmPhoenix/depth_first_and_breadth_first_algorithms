def breadth_first_algorithm(graph, source):
    queue = [source]

    while(len(queue) > 0):
        current = queue.pop()
        print(current)

        for neighbor in graph[current]:
            queue.insert(0, neighbor)


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

breadth_first_algorithm(graph, 'a')
