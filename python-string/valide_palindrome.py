class Solution:

    def is_palndrome(self, s : str ) -> bool:
        temp_forward_string =  s

        reversed_string = s[::-1]

        if temp_forward_string == reversed_string:
            return True
        else:
            return False


obj = Solution()
print(obj.is_palndrome("mydam"))