#If you are given a sorted array -> two pointer strategy

# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

#EXAMPLES

# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

def pair_with_targetsum(arr, target_sum):
    #TWO POINTER STRATEGY
    #TIME COMPLEXITY : 0(N)
    #SPACE COMPLEXITY : 0(1)

    i, j = 0, len(arr) - 1 
    current_sum = 0

    while(i < j):
        current_sum = arr[i] + arr[j]
        if current_sum < target_sum:
            # need to increase an operand, increase lowest pointer
            i += 1
        elif current_sum > target_sum:
            #need to decrease an operand, decrease largest pointer
            j -= 1
        else:
            #we found a match
            return [i,j]


    #return a pair of indeces in an array
    return [-1,-1]
# TESTS

assert [1,3] == pair_with_targetsum([1, 2, 3, 4, 6], 6)
assert [0,2] == pair_with_targetsum([2, 5, 9, 11], 11)

#ALTERNATE SOLUTION USING HASHMAP
def pair_with_targetsum_hash(arr, target_sum):
    #TIME COMPLEXITY : 0(N)
    #SPACE COMPLEXITY O(N)

    indeces = {}

    #If you ever find needing both the index and the element, consider enumerate()
    for i, num in enumerate(arr):
        if target_sum-num in indeces:
            return [indeces[target_sum-num] , i]
        else:
            indeces[num] = i
    return [-1,-1]

assert [1,3] == pair_with_targetsum_hash([1, 2, 3, 4, 6], 6)
assert [0,2] == pair_with_targetsum_hash([2, 5, 9, 11], 11)