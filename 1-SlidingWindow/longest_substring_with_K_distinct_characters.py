# Given a string, find the length of the longest substring in it with 
# no more than K distinct characters.

# EXAMPLES

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longest_substring_with_k_distinct(str, k):
    #TIME COMPLEXITY = O(N)
    #SPACE COMPLEXITY = 0(K) since we are storing at most k+1 characters in the hashmap

    longest_length = 0
    window_start = 0
    #we need to remember the frequency of letters -> hashmap
    frequency = {}
    
    for window_end in range(len(str)):
        #when expanding the window -> manipulate window_end
        end_char = str[window_end]
        
        #example of how length of the window is determined by a different condition other than pure length
        if end_char not in frequency:
            frequency[end_char] = 0
        frequency[end_char]+=1

        #len(frequency) gives the number of keys
        while len(frequency) > k:
            #shrink window -> manipulate window_start
            start_char =str[window_start]
            frequency[start_char] -= 1

            if frequency[start_char] == 0:
                del frequency[start_char] #delete key, value pair
            window_start += 1
        
        longest_length = max(longest_length , window_end - window_start + 1)
    return longest_length


    
# TESTS
assert 4 == longest_substring_with_k_distinct("araaci",2)
assert 2 == longest_substring_with_k_distinct("arraci", 1)
assert 5 == longest_substring_with_k_distinct("cbbebi", 3)