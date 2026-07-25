class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palindrome = []

        for val in s:
            ascii_val = ord(val)

            if ((ascii_val >= 48 and ascii_val <= 57)
                or (ascii_val >= 65 and ascii_val <= 90)
                or (ascii_val >= 97 and ascii_val <= 122)):
                
                palindrome.append(val.lower())

        
        return palindrome == palindrome[::-1]
        