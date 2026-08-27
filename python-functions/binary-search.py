class Solution:

    def binary_search(self, nums: list, target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1

            elif target > nums[mid]:
                left = mid + 1

            else:
                return mid

        return -1



obj = Solution()

nums = [1, 3, 5, 7, 9, 11, 13, 15]

print(obj.binary_search(nums, 131))