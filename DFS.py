from collections import deque

def dfs(graph, start , visited = None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)


graph = {
   'A' : ['B','C'],
   'B' : ['A','D','E'],
   'C' : ['A','F','G'],
   'D' : ['B'],
   'E' : ['B'],
   'F' : ['C'],
   'G' : ['C']
}
print("The DFS for the given graph is: ")
dfs(graph, 'A')