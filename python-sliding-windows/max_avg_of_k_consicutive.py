nums = [1, 12, -5, -6, 50, 3]
k = 4

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
    
print(max_sum/k)