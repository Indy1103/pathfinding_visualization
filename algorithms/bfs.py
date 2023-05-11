from collections import deque

def bfs(graph, start, callback=None):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if callback:
                callback(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited