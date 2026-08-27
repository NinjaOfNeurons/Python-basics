# [1,3,4,5] , [2,4,6,8] 

class Solution:
    def merge_sorted_array(self, nums1:list,nums2:list)-> list:
        i = 0 
        j = 0 
        nums = []
        while(i < len(nums1) and j < len(nums2)):
            
            if(nums1[i] <= nums2[j]):
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])

                j+=1



        while i < len(nums1):
            nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums.append(nums2[j])
            
            j+=1

        return nums




obj = Solution()
print(obj.merge_sorted_array([1,3,4,5] , [2,4,6,8] ))