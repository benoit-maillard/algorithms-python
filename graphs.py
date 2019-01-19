import math

from collections import deque

def bfs(graph, start):
    nodes_queue = deque([start])
    distances = [math.inf for v in graph]
    distances[start] = 0

    while len(nodes_queue) != 0:
        current = nodes_queue.pop()

        for v in graph[current]:
            if distances[v] == math.inf:
                distances[v] = distances[current] + 1
                nodes_queue.appendleft(v)

    return distances

def dfs(graph, start):
    times = [[math.inf, math.inf] for v in graph]
    colors = [0 for v in graph] # 0 : white, 1 : grey, 2 : black

    def dfs_visit(node, disc_time):
        colors[node] = 1 # the node turns grey
        times[node][0] = disc_time

        current_time = disc_time
        for v in graph[node]:
            if colors[v] == 0:

                current_time += 1
                current_time = dfs_visit(v, current_time)

        times[node][1] = current_time + 1
        colors[node] = 2
        return current_time + 1

    dfs_visit(start, 0)

    return (times, colors)

def reverse(graph):
    new = [[] for v in graph]
    for i in range(len(graph)):
        for u in graph[i]:
            new[u].append(i)
    
    return new

def prim()

undirected_graph = [
    [1, 3],
    [0, 2],
    [1, 3, 6],
    [0, 2, 4],
    [3, 5, 6],
    [4],
    [2, 4, 7],
    [6, 8, 9],
    [7, 9],
    [7, 8, 10],
    [9]
]

directed_graph = [
    [1, 5],
    [2, 6],
    [3, 7],
    [9],
    [4, 7, 8, 9],
    [6],
    [0, 7],
    [2],
    [9],
    [4]
]

b = bfs(undirected_graph, 0)
d = dfs(undirected_graph, 0)

print(reverse(directed_graph))