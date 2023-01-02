# is there any path between source (src) and destination (dst)?
# you can use breadth first algorithm to find out

def has_path_BF(graph, src, dst):
    queue = [src]

    while(len(queue) > 0):
        current = queue.pop()
        if(current == dst): return True

        for neighbor in graph[current]:
            queue.insert(0, neighbor)

    return False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path_BF(graph, 'f', 'k'))

print(has_path_BF(graph, 'j', 'f'))
