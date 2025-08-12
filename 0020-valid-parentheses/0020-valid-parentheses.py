class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets_dict = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for i in s:
            if i in brackets_dict:
                if stack and stack[-1] == brackets_dict[i]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)
        
        return True if not stack else False