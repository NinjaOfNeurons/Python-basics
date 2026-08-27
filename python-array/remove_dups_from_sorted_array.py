class Solution:
    def Remove_dup(self, given_list : list )-> list:
        my_set = []
        for i in range(len(given_list)-1):  
            if given_list[i] == given_list[i+1]:
                continue
            else: 
                my_set[i] = given_list[i]

        return my_set


    def Remove_dup_set(self, given_list: list) -> list:
        lis = list(set(given_list))
        lis.sort()
        return lis

obj = Solution()
print(obj.Remove_dup_set([2, 7, 9, 15]))


