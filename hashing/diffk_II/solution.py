# given a array , and non-negative integer k ,find if there exist 2 indices i and j such that such that A[i] - A[j] = k and i != j
def diffk(arr,k):
    hash_map = set()
    length = len(arr)
    arr.sort()
    for i in range(0,length):
        diff = arr[i] - k
        if diff in hash_map:
            return True
        else:
            hash_map.add(arr[i])
    return False

# test case
arr = [1,5,3]
k = 2
ans = diffk(arr,k)
print(ans)