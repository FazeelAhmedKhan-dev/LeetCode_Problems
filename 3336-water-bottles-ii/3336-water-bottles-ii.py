class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        bottlesDrunk = numBottles

        while numBottles >= numExchange:
            numBottles -= numExchange
            numBottles += 1
            bottlesDrunk += 1
            numExchange += 1 

        return bottlesDrunk
        