# [0, 1, 0, 3, 12]



class Solution:
    def Reverse_list(self, nums : list , start : int, end : int):

        i = start
        j = end

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums

p = Solution()


nums =[1,2,3,4,5,6,7]
k = 8
k = k % len(nums)

print(p.Reverse_list(nums , 0, len(nums) - 1  ))
print(p.Reverse_list(nums, 0, k-1))
print(p.Reverse_list(nums, k , len(nums) - 1))

