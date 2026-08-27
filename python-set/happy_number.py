class Solution:
    def happy_num(self, num):
        seen = set()
        total = 0 
        while True:

            total = 0

            while(num > 0 ):
                last_digit = num % 10
                total += last_digit ** 2
                num = num // 10

            if total not in seen:
                seen.add(total)
            else:
                return False

            if total == 1:
                return True


            num = total 


obj = Solution()
print(obj.happy_num(19))

            


            
