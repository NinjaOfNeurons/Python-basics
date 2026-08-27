class Solution:


    def is_have_dup_set(self, nums : list )->bool:
        seen = set( )
        for num in nums:
            # print(num)
            if num in seen:
                return True
            else:
                seen.add(num)
        return False           
        


obj = Solution()

print(obj.is_have_dup_set([2, 7, 3, 7]))


