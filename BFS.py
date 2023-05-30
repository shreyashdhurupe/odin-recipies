def bfs(node):
    visited = [False] * (len(graph))
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

graph = {
   'A' : ['B','C'],
   'B' : ['A','D','E'],
   'C' : ['A','F','G'],
   'D' : ['B'],
   'E' : ['B'],
   'F' : ['C'],
   'G' : ['C']
}


bfs('A')