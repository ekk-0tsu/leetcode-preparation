from collections import defaultdict

def calcEquation(equations, values, queries):
    graph = defaultdict(dict)
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1 / val
    visited = set()

    # Define DFS function
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        print(start, end)
        visited.add(start)
        for neighbor, weight in graph[start].items():
            if neighbor not in visited:
                res = dfs(neighbor, end, visited)
                print(res, weight)
                if res != -1.0:
                    return weight * res
        return -1.0

    # Process queries
    results = []
    for (a, b) in queries:
        results.append(dfs(a, b, set()))

    return results

r = calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["c","a"],["x","x"]])
print(r)

