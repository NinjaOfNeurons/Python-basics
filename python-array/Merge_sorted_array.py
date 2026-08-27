class Solution:
    def is_have_dup(self, ar1 : list , ar2 :list )-> list:
        i = 0 
        j = 0 
        # k = 0
        ar3=[]
        while(i < len(ar1) and j < len(ar2)):
            if ar1[i] <= ar2[j]:
                ar3.append(ar1[i])
                # k += 1
                i += 1
            else:
                ar3.append(ar2[j])
                # k += 1
                j += 1


        while i < len(ar1):
            ar3.append(ar1[i])
            i += 1

        while j < len(ar2):
            ar3.append(ar2[j])
            j += 1

        return ar3


     

obj = Solution()
print(obj.is_have_dup([1,3,4,5] , [2,4,6,8] ))


