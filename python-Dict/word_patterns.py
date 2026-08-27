class Solution:

    def is_isomorphic(self, pattern: str, s: str) -> bool:
        s_to_pattern = {} 
        pattern_to_s = {}
        s = s.split()

        if len(pattern) != len(s):
            return False
        
        for i in range(len(s)):

            if s[i] not in s_to_pattern:
                s_to_pattern[s[i]] = pattern[i]

            if pattern[i] not in pattern_to_s:
                pattern_to_s[pattern[i]] = s[i]

            if s_to_pattern[s[i]] != pattern[i]:
                return False

            if pattern_to_s[pattern[i]] != s[i]:
                return False

        print(s_to_pattern,pattern_to_s)

        return True


obj = Solution()
pattern = "abba"
s = "dog cat cat fish"

print(obj.is_isomorphic(pattern, s))