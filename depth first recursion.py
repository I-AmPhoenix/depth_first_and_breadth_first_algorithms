def depth_first_algorithm_recursion_version(graph, source):
    print(source)

    for neighbor in graph[source]:
        depth_first_algorithm_recursion_version(graph, neighbor)


graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

depth_first_algorithm_recursion_version(graph, 'a')
