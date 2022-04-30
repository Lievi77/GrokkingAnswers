#SLIDING WINDOW: USUALLY USED WHEN WE ARE DEALING WITH CONTIGUOUS ARRAYS

# PROBLEM:
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# EXAMPLES:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].
import math
def max_sub_array_of_size_k(k, arr):
    #TIME COMPLEXITY  O(N)
    #SPACE COMPLEXITY 0(1) 

    #SLIDING WINDOW
    windowStart = 0 
    windowSum = 0
    maxSum = - math.inf

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if(windowEnd >= k-1):
            #check maxSum 
            maxSum = max(maxSum, windowSum)

            #Slide window
            #by sliding, we mean substracting the first element and 
            # advancing 
            windowSum -= arr[windowStart]
            windowStart +=1

    return maxSum


#TESTS
assert 9 == max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])
assert 7 == max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])
# print(max_sub_array_of_size_k(2,[-1,-2,-3,-4,-1]))
