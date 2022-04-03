# create a list of the first 6 positive numbers divisible by 5
fiveList = []

i = 0
while len(fiveList) < 6:
    if i%5==0:
        if i!=0:
            fiveList.append(i)
        i += 5

print(fiveList)

#Add to the list the next number dividable by 5 (it will be the seventh number).
fiveList.append(fiveList[-1]+5)
print(fiveList)

#Print the length of the list.
print(len(fiveList))

#Print the second to 4th number.
print(fiveList[1:4])

#Print numbers from the first up until the one before last.
print(fiveList[0:-1])