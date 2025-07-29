class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0

        for i in accounts:
            curr_wealth = sum(i)
            wealth = max(wealth, curr_wealth)
        
        return wealth