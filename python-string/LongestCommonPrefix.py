class solution:

    def common_str(self, ch1 : str, ch2 : str )-> str:
        prefix_val = ""

        for i in range(min(len(ch1), len(ch2))):
            if ch1[i] == ch2[i]:
                prefix_val = prefix_val + ch1[i]

            else:
                break

        return prefix_val



prefix_obj = solution()

list_str = ["flower", "flow", "flight"]

current_prefix = list_str[0]

for i in range(1, len(list_str)):
   current_prefix = prefix_obj.common_str(current_prefix, list_str[i])

print(current_prefix)

# print(prefix_obj.common_str("flower", "flow"))

