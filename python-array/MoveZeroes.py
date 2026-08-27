# [0, 1, 0, 3, 12]



class Solution:
    def move_it(self, nums : list)-> list:
        k = 0
        for num in nums:
            if num == 0:
                continue
            else: 
                nums[k] = num 
                k += 1
        # print(nums)

        while(k <= len(nums) - 1 ):
            nums[k] = 0
            k += 1

        return nums

p = Solution()
print(p.move_it([0,1,0,3,12]))

