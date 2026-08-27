class Solution:
    def intersection_array(self, nums1 : list, nums2 : list)-> list:
        i = 0
        j = 0
        s = set()
        nums1.sort()
        nums2.sort()

        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i] == nums2[j]):
                s.add(nums1[i])

                i = i+1
                j = j+1
            else:
                i += 1
        return s


    def intersection_array_dict(self, nums1 : list, nums2 : list)-> list:
        i = 0
        j = 0
        s = set()
        dict = {}
        for num in nums1:
            dict[num] = 1


        print(dict)
        for num in nums2:
            if num in dict:
                s.add(num)
        
        return s

                

                


obj = Solution()
nums1 = [1,7,3]
nums2 = [3,7,9]
print(obj.intersection_array_dict(nums1,nums2))