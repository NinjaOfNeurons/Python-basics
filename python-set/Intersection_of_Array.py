class Solution:


    def arrayintersection(self, nums1 : list, nums2 : list )->set:
        seen = set(nums1)
        set_2 = set()
        for num in nums2:
            # print(num)
            if num in seen:
                set_2.add(num)
        return set_2           
        


obj = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2,1]
print(obj.arrayintersection(nums1, nums2))


