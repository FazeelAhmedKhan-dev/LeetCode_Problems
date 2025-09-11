class Solution:
    def sortVowels(self, s: str) -> str:
            
        s = list(s)
        vowels = {"a", "e", "i", "o", "u"}
        vowels_in_str = []
        
        for i in range(len(s)):
            if s[i].lower() in vowels:
                vowels_in_str.append(ord(s[i]))
        vowels_in_str.sort()
        for j in range(len(s)):
            if s[j].lower() in vowels:
                s[j] = chr(vowels_in_str[0])
                vowels_in_str.pop(0)
        
        return "".join(s)