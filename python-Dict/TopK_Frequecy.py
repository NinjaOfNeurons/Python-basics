class Solution:

    def get_frequency(self, item):
        return item[1]

    def topk(self, nums: list, k: int) -> list:

        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        sorted_freq = sorted(
            freq_dict.items(),
            key=self.get_frequency,
            reverse=True
        )

        result = []

        for items in sorted_freq[:k]:
            result.append(items[0])

        return result


obj = Solution()

nums = [1, 1, 1, 3, 3, 2]
k = 2

result = obj.topk(nums, k)

print(result)