
def findMissingNumber2(array1, array2):
    d=collections.defaultdict(int)
    for num in array2:
        d[num]+=1
    for num in array1:
        if d[num]==0:
            return num
        else:
            d[num]-=1
