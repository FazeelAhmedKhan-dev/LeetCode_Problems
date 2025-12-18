class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i , total, curr):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i, total + candidates[i] ,curr)

            curr.pop()
            dfs(i+1, total, curr)
        
        dfs(0, 0, [])
        return res
