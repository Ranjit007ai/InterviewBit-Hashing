# given a array ,find the four numbers whose sum matches a given target value
def four_sum(arr,target):
    length = len(arr)
    arr.sort()
    A = []
    for i in range(0,length):
        for j in range(i+1,length):
            k = j + 1
            l = length - 1
            while k < l:
                if arr[i] + arr[j] + arr[k] + arr[l] < target:
                    k += 1
                elif arr[i] + arr[j] + arr[k] + arr[l] > target:
                    l -= 1
                elif arr[i] + arr[j] + arr[k] + arr[l] == target:
                    if [arr[i],arr[j] ,arr[k],arr[l]] not in A:
                        A.append([arr[i],arr[j] ,arr[k],arr[l]]) 
                        k += 1
                        l -= 1
    return A 

# test case
arr = [1,0,-1,0,-2,2]
target = 0
ans = four_sum(arr,target)
print(ans)