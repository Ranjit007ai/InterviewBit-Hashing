# Given a number ,we must say if it is a colorful number or not.
# A number is colorful number , if product of each contigous subsequence of it is different.
# ex : 3245 3 2 4 5 32 24 45 324 245 =>product => 3 2 4 6 8 20 24 40 ,since all product are different so it is color full number.

def is_colorful_number(number): 
    number = str(number)
    length = len(number)
    hash_map = set() # set to store the product values
    for i in range(0,length):
        product = 1
        for j in range(i,length):
            product *= int(number[j])

            if product in hash_map:
                return False
            hash_map.add(product)
    return True

# test case
number = 3245
ans = is_colorful_number(number)
print(ans)

