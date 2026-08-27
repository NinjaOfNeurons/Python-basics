class Solution:
    def is_subsequence(self, og_string : str, sub_string : str) -> bool:

        i = 0 
        j = 0

        while(i != len(og_string) and j != len(sub_string)):
            if og_string[i] == sub_string[j]:
                i += 1
                j += 1
            else:
                i += 1


        return j == len(sub_string)
        
            
        
p = Solution()
print(p.is_subsequence("abc","a"))

