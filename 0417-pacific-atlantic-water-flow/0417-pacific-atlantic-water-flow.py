from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def dfs(r, c, visited):
            visited[r][c] = True
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and 
                    not visited[nr][nc] and 
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)

        # Pacific Ocean (top and left borders)
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)

        # Atlantic Ocean (bottom and right borders)
        for i in range(m):
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(m-1, j, atlantic)

        # Cells reachable by both
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])

        return result