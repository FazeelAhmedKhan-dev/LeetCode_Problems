class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = int("".join(map(str,digits)))
        num += 1
        num = str(num)

        for index, val in enumerate(num):
            if index + 1 > len(digits):
                digits.append(int(val))
            else:
                digits[index] = int(val)
            
        return digits