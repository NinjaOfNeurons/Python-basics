class Solution:
    def is_have_dup(self, given_list : list )-> bool:
        given_list.sort()

        for i in range(len(given_list)-1):
            if given_list[i] == given_list[i+1]:
                return True
        return False
        

    def is_have_dup_while(self, given_list: list) -> bool:
        given_list.sort()

        i = 0
        j = i + 1

        while i < len(given_list) and j < len(given_list):

            if given_list[i] == given_list[j]:
                return True

            else:
                i += 1
                j += 1

        return False


    def is_have_dup_dict(self, given_list : list )->bool:
        freq_num = {}
        for num in given_list:
            freq_num[num] = freq_num.get(num, 0) + 1

        print(freq_num)
        for val in freq_num.values():
            if val > 1:
                return True
                

        return False

    def is_dup_dict_cheat(self, given_list : list )->bool:
        dic = {}
        for i in given_list:
            if i in dic:
                return True
            dic[i] = 1
        return False



obj = Solution()
print(obj.is_dup_dict_cheat([2, 7, 3, 7]))


