def findBigestNum(num) :
    bigest = num[0]
    for i in num :
        if i > bigest:
            bigest = i
    return(bigest)

listnum = [4, 5, 17, 3, 2, 9]

print(findBigestNum(listnum))
print(max(listnum))
print(min(listnum))
