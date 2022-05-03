# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

#EXAMPLES
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

def remove_duplicates(arr):
    #TIME COMPLEXITY : 0(N)
    # SPACE COMPLEXITY : O(1)

    #TWO Pointers
    next_non_dup = 1 #we know that the first element is unique
    #pointer indicates the next-non duplicate element

    for j in range(1, len(arr)):
        #if the previous non-duplicate element is not equal to the current pointer
        if arr[next_non_dup - 1] != arr[j]:
            arr[next_non_dup] = arr[j] #place current element (non-duplicate) in the next non duplicate position
            next_non_dup +=1 #increment duplicate pointer
    return next_non_dup 

# TESTS
assert 4 == remove_duplicates([2, 3, 3, 3, 6, 9, 9])
assert 2 == remove_duplicates([2, 2, 2, 11])

# A similar question

# Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

#unsorted -> means we cannot guarantee the first element to  be unique

#EXAMPLES 

# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

# Input: [2, 11, 2, 2, 1], Key=2
# Output: 2
# Explanation: The first two elements after removing every 'Key' will be [11, 1].

# Very similar question use a two pointer strategy

def remove_element(arr,key):
    nextElement = 0 #pointer to signalize the end of the filtered array

    for j in range( len(arr)):
        if arr[j] != key:
            arr[nextElement] = arr[j]
            nextElement +=1
    return nextElement

assert 4 == remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)
assert 2 == remove_element([2, 11, 2, 2, 1],2)

