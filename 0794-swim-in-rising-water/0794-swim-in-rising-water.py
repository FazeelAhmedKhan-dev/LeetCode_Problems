class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        while min_heap:
            t, i, j = heapq.heappop(min_heap)
            res = max(res, t)
            if (i, j) == (n - 1, n - 1):
                return res
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(min_heap, (grid[ni][nj], ni, nj))
        return t