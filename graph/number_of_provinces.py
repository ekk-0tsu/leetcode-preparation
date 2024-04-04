# Solution using DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:   
        m = len(isConnected)
        n = len(isConnected[0])

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for i in range(n):
                if isConnected[node][i] == 1:
                    dfs(i)
            return
        
        visited = set()
        provinces = 0
        for i in range(m):
            if i not in visited:
                dfs(i)
                provinces += 1
        
        return provinces

# Solution returning the number of provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            for i in range(n):
                if isConnected[node][i] == 1:
                    dfs(i)
            
            return 1
        
        for i in range(n):
            if i not in visited:
                provinces += dfs(i)
        
        return provinces
