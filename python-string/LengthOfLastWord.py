class Solution:
    def len_last_word(self, sent : str)-> int:
        rev_sent = sent[::-1]

        rev_sent = rev_sent.strip()  #removing extra spaces

        first_space = len(rev_sent) #if first space is not found then whole sentence is first space 

        for index, ch in enumerate(rev_sent):
            if ch == " ":
                first_space = index
                break

        return len(rev_sent[:first_space])





obj = Solution()

print(obj.len_last_word("Hello"))


