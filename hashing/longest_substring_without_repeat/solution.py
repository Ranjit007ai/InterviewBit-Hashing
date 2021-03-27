# given a string, find the length of longest substring without repeating characters.
#ex : "abcabcbb" is "abc" length = 3

def length_of_longest_substring(A):
    length = len(A)
    max_length = 0
    hash_map = {}
    left,right = 0,0
    while right < length :
        if A[right] in hash_map:
            left = max(left,hash_map[A[right]]+1)
        hash_map[A[right]] = right
        max_length = max(max_length,right - left + 1)
        right += 1
    return max_length

# test cas
A = "abcabcbb"
ans = length_of_longest_substring(A)
print(ans)