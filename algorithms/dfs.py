
def dfs(graph, start, visited=None, callback=None):
    if visited is None:
        visited = []

    visited.append(start)
    if callback:
        callback(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, callback)

    return visited