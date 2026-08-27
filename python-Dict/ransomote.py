class Solution:

    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        mag_dic = {}
        for note in magazine:
           mag_dic[note] = mag_dic.get(note, 0 ) + 1

        for word in ransom_note:

            if word not in mag_dic:
                return False

            if mag_dic[word] == 0:
                return False 

            mag_dic[ word] -= 1
        
        return True
        # for key, val in mag_dic.items():
        #     if val == 0:
        #         return True
        # # print(mag_dic)  

        # return False      


obj = Solution()
print(obj.can_construct("ac","aabc"))    
           