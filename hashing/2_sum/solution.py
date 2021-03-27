# given a array , find two numbers whose sums match the given target value
def two_sum(arr,target): 
    hash_map = {} # dictionary to store the value and the correspounding index position.
    length = len(arr)
    for i in range(0,length):
        diff = target - arr[i]
        if diff in hash_map:
            return i,hash_map[diff] 
        else:
            hash_map[arr[i]] = i 
        
# test case
arr = [2,7,11,15]
target = 26
ans = two_sum(arr,target)
print(ans)