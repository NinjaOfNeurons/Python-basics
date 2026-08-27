class Solution:

    def rev_stng(self, word: str)-> str:
        result = []
        rev_filter = word[::-1].split()

        for i in range(len(rev_filter)):
            new_word = rev_filter[i][::-1]
            result.append(new_word)

        final_word = " ".join(result)
        return final_word


obj = Solution()
print(obj.rev_stng("my   is"))
