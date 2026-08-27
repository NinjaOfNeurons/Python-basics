class Solution:

    def is_isomorphic(self, s: str, t: str) -> bool:
        s_to_t = {} 
        t_to_s = {}
        for i in range(len(s)):
            if s[i] not in s_to_t:
                s_to_t[s[i]] = t[i]

            if t[i] not in t_to_s:
                t_to_s[t[i]] = s[i]

            if s_to_t[s[i]] != t[i]:
                return False

            if t_to_s[t[i]] != s[i]:
                return False

        print(s_to_t, t_to_s)

        return True


obj = Solution()

print(obj.is_isomorphic("foo", "bar"))