class Solution:
    def Remove_dup(self, nums : list )-> list:
        return list(set(nums))


    def Remove_dup_2pointer(self, nums : list )-> list:
        i = 0 
        j = 1
        while(j < len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            else:
                j += 1

        return(nums[:i+1])



    

obj = Solution()
print(obj.Remove_dup_2pointer([2, 4, 4, 7, 15,15]))


