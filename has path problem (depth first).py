# is there any path between source (src) and destination (dst)?
# you can use depth first algorithm to find out

def has_path_DF(graph, src, dst):
    if(src == dst): return True

    for neighbor in graph[src]:
        if(has_path_DF(graph, neighbor, dst)== True):
            return True
    return False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path_DF(graph, 'f', 'k'))
