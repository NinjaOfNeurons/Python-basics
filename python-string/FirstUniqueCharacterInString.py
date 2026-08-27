class solution():

    def first_unique_char(self, word) :
        count = {}
        for ch in word:
            count[ch] = count.get(ch, 0) + 1



        for index, ch in enumerate(word):
            if count[ch] == 1:
                return index
        return -1



obj = solution()


my_word = "aakaa"



index_first_uniue = obj.first_unique_char("aakaa")

print(my_word[index_first_uniue])