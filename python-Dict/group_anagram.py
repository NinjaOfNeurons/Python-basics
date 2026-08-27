

class Solution:
    def group_anagram(self, words : list)-> dict:
        dict_ = {}
        
        for ch in words:
            ch_sort = "".join(sorted(ch))

            if ch_sort not in dict_:    # initially we have a empty dict so we did this to create a aet -->eat dict  
                dict_[ch_sort] = [ch]
                
            else:
                dict_[ch_sort].append(ch)  #now since we have aet so we append
        
            
        return dict_



obj = Solution()
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict_ = obj.group_anagram(words)
print(dict_)