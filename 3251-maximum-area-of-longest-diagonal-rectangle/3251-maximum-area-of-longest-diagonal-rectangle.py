class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        curr_diagonal = 0
        max_area = 0
        
        for i in dimensions:
            curr_diagonal = (i[0] ** 2) + (i[1] ** 2)
            if curr_diagonal > max_diagonal:
                max_area = i[0] * i[1]
                max_diagonal = curr_diagonal
            elif curr_diagonal == max_diagonal:
                max_area = max(max_area, i[0] * i[1])
            else:
                max_diagonal = max(max_diagonal, curr_diagonal)
        
        return max_area