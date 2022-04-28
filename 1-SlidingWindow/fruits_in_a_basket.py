# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

#EXAMPLES
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

# The phrase "you can't skip a tree" implies a contingent solution

def fruits_into_baskets(fruits):
    #two baskets 
    max_fruits = 0
    window_start = 0
    basket = {}

    for window_end in range(len(fruits)):
        end_fruit = fruits[window_end]

        if end_fruit not in basket:
            basket[end_fruit] = 0
        basket[end_fruit] += 1

        #shrink window 
        while len(basket) > 2:
            start_fruit = fruits[window_start]
            basket[start_fruit] -= 1
            if basket[start_fruit] == 0:
                del basket[start_fruit]
            window_start += 1
        
        max_fruits = max(max_fruits , window_end - window_start + 1)

    return max_fruits

# TESTS 
assert 3 == fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
assert 5 == fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])