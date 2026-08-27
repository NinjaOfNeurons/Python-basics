class Solution:
    def two_sum(self, my_list :  list, target : int)-> tuple:
        list_dict = {}
        for index ,  val in enumerate(my_list):
            needed = target - val
            if needed in list_dict:
                return(index, list_dict[needed])
            else:
                list_dict[val] = index 




obj = Solution()
print(obj.two_sum([2,7,11,15],29))
















# class Solution:
#     def two_sum(self, my_list :  list, target : int)-> tuple:
#         my_list.sort()

#         i = 0
#         j = len(my_list) -1

#         while(i < len(my_list) and j >= 0 ):
#             if(my_list[i] + my_list[j] > target ):

#                 j = j - 1
#             elif(my_list[i] + my_list[j] < target ):

#                 i += 1 
#             else:
#                 return(i,j)  
            


