class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        m = len(languages)
    
        candidates = set()
        for u, v in friendships:
            u_langs = set(languages[u-1])
            v_langs = set(languages[v-1])
            if u_langs.isdisjoint(v_langs):
                candidates.add(u)
                candidates.add(v)

        min_teach = float('inf')
        for lang in range(1, n+1):
            count = 0
            for user in candidates:
                if lang in languages[user-1]:
                    count += 1
            teach_needed = len(candidates) - count
            min_teach = min(min_teach, teach_needed)

        return min_teach