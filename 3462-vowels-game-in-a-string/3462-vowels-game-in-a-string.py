class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}
        vowels_in_str = set()
        for i in s:
            if i in vowels:
                vowels_in_str.add(i)
        
        n = len(vowels_in_str)
        if n == 0:
            return False
        elif n % 2 != 0:
            return True
        else:
            return True