# Given an array of positive numbers and a positive number ‘S’, 
#find the length of the smallest contiguous subarray whose sum 
#is greater than or equal to ‘S’. Return 0, if no such subarray exists.

#EXAMPLES

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

import math 
def smallest_subarray_with_given_sum(s,arr):
    #Regular sliding window problem except that window's size is not fixed

    # Sum of subarray must be equal or greater than s
    window_sum = 0
    min_length = math.inf #answer
    window_start = 0

    for window_end in range(len(arr)):
        #expand window until sum >= s
        window_sum += arr[window_end]
 
        #shrink window once sum >= s
        while(window_sum >= s):
            window_length = window_end - window_start + 1 
            min_length = min(min_length, window_length)

            window_sum -= arr[window_start] #substract start
            window_start +=1 #shrink window
    if min_length == math.inf:
        return 0
    
    return min_length

#TESTS
assert 2 == smallest_subarray_with_given_sum( 7, [2,1,5,2,3,2])
assert 1 == smallest_subarray_with_given_sum( 7, [2,1,5,2,8])
assert 3 == smallest_subarray_with_given_sum( 8, [3,4,1,1,6])