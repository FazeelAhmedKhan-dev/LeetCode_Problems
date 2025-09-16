class Solution:

    def find_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack:
                g = self.find_gcd(stack[-1], num)
                if g > 1:
                    num = stack[-1] * num // g 
                    stack.pop()
                else:
                    break
            stack.append(num)
        return stack