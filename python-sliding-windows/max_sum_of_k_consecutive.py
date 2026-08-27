nums = [2, 1, 5, 1, 3, 2]
k = 3

left = 0 
right = k-1

window_sum = sum(nums[left:right + 1])
max_sum = window_sum

while(right + 1 < len(nums)):

    window_sum = window_sum - nums[left]

    left+=1
    right+=1

    window_sum = window_sum + nums[right]

    max_sum   = max(window_sum, max_sum)
    
print(max_sum)