# Given a string, find the length of the longest substring which has no repeating characters.

#substring -> contingent solution

# EXAMPLES

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

def non_repeat_substring(str):
    #Time Complexity O(N)
    #Space Complexity 0(K), K is the number of distinct characters in the string

    #in interviews, use i,j
    max_length = 0
    i = 0
    characters = {} # we will store each character with its last index

    for j in range(len(str)):
        end_char = str[j]

        #shrink sliding window if we have an occurance
        if end_char in characters:
            #incoming end char violates problem's constraint
            i =  max(i,characters[end_char] +1 )
        
        characters[end_char] = j 
        max_length = max(max_length, j - i + 1)

    return max_length

#TESTS 
assert 3 == non_repeat_substring("aabccbb")
assert 2 == non_repeat_substring("abbbb")
assert 3 == non_repeat_substring("abccde")
\
