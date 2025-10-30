class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram = {}

        for i in range(len(strs)):
            sort_chr = sorted(strs[i])
            sort_str = "".join(sort_chr)

            if sort_str not in anagram:
                anagram[sort_str] = [strs[i]]
            
            else:
                anagram[sort_str].append(strs[i])
            
        return [anagram[an] for an in anagram]
