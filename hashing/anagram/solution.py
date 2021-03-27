# given a array of words, return the list of all anagram
# ex : [cat,act,dog,tac,god] => o/p : [[1,2,4],[3,5]]
def anagram(arr):
    duplicate_arr = []
    hash_map = {} # dictionary to store the anagram and their index
    final_output = []
    for i in range(0,len(arr)):
        cur_word = arr[i]
        cur_word = sorted(cur_word)
        cur_word = ''.join(cur_word)
        duplicate_arr.append(cur_word)
    for i in range(0,len(duplicate_arr)):
        word = duplicate_arr[i]
        if word in hash_map:
            hash_map[word].append(i+1)
        else:
            hash_map[word] = [i+1]
    for i in hash_map:
        final_output.append(hash_map[i])
    return final_output

# test case
arr = ['cat','dog','act','god','tac']
ans = anagram(arr)
print(ans)