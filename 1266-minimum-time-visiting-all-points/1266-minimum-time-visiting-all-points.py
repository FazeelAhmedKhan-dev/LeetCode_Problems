class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        steps = 0

        for i in range(n-1):

            x1 = points[i][0]
            y1 = points[i][1]

            x2 = points[i+1][0]
            y2 = points[i+1][1]

            dy = abs(y2-y1)
            dx = abs(x2-x1)

            steps += (min(dx, dy) + abs(dy-dx))
        return steps
        