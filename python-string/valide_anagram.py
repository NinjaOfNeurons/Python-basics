class Solution:

    def is_anagram(self, s1 : str, s2 : str ) -> bool:
        if len(s1)==len(s2):
            return sorted(s1) == sorted(s2)
        else:
            return False



ang = Solution()
print(ang.is_anagram("karan", "ranka"))