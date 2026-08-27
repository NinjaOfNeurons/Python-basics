class Solution:

    def plus_1(self, nums : list)-> list:
        i = len(nums) -1 
        while(i>=0):
            # print(i)
            if nums[i] < 9:
                nums[i] += 1
                return nums
            else:
                nums[i] = 0   

            i -= 1

        return [1] + nums


obj = Solution()
# nums1 = [1,7,3,3]
nums1 = [8,9,9]
print(obj.plus_1(nums1))