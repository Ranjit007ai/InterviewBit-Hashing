# find the largest continous sequence in the array which sums to zero.
def largest_sequence_zero(Arr):
    hash_map = {} # dictionary to store the sum and the correspounding index
    sums = 0
    max_len = 0
    max_array = []
    for i in range(0,len(Arr)):
        sums += Arr[i]
        if Arr[i] == 0 and max_len == 0:
            max_len = 1
            max_array = Arr[i:i+1]
        if sums == 0:
            max_len = i + 1
            max_array = Arr[:i+1]
        if sums in hash_map :
            diff = i - hash_map[sums]
            if diff > max_len:
                k = hash_map[sums] + 1
                max_len = diff
                max_array = Arr[k:i+1]
        else:
            hash_map[sums] = i
    return max_array

# test case
arr = [1,2,-2,4,-4]
ans = largest_sequence_zero(arr)        
print(ans)