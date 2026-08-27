class Solution:

    def majority_elem(self, nums : list)-> int:

        num_dic = {}
        for num in nums:
            num_dic[num] =  num_dic.get(num, 0) + 1
        # print(num_dic)

        criteria = len(nums) // 2  # absolute division

        for key, val in num_dic.items():
            if val > criteria:
                return(key)

        return None


obj = Solution()
nums1 = [1,7,3,3]
# nums2 = [3,7,9]
print(obj.majority_elem(nums1))