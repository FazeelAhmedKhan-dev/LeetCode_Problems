class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        res = 0
        neg_count = 0
        min_num = float("inf")

        for rows in range(len(matrix)):
            for cols in range(len(matrix[rows])):
                res += abs(matrix[rows][cols])
                min_num = min(min_num, abs(matrix[rows][cols]))

                if matrix[rows][cols] < 0:
                    neg_count += 1
        
        if neg_count % 2 != 0:
            res -= 2 * min_num

        return res
