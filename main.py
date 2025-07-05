def DFS(start, graph, visited = None):
    if (visited == None):
        return
    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(neighbor, graph, visited)