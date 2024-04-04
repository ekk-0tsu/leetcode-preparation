class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x1, y1, ocean):
            if (x1, y1) in ocean:
                return

            ocean.add((x1, y1))

            for dx, dy in dirs:
                x2 = x1 + dx
                y2 = y2 + dy

                if 0 <= x2 < m and 0 <= y2 < n and heights[x2][y2] >= heights[x1][y2]:
                    dfs(x2, y2, ocean)

        for i in range(m):
            dfs(m - 1, 0, pacific)
            dfs(i, n - 1, atlantic)

        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return list(pacific.intersection(atlantic))

