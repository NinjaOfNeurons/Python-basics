class Solution:
    def happy_num(self, n):
        seen = set()
        while True:
            total = 0

            while(n > 0):
                last_digit = n % 10
                total += last_digit ** 2
                n = n // 10

            if total == 1:
                return True

            if total in seen:
                return False

            seen.add(total)
            
            n = total

obj = Solution()
print(obj.happy_num(19))

            


            
