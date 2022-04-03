#populating fiveList below:
fiveListB = []

i = 0
while len(fiveListB) < 7:
    if i%5==0:
        if i!=0:
            fiveListB.append(i)
        i += 5


#Reverse the list and print it.
fiveListB.reverse()
print(fiveListB)

# Remove the middle element from the list and print the list.
middleElement = fiveListB.pop(3)
print(fiveListB)

#Print the sum, the maximal value and the average value from the list.
print(sum(fiveListB))

print(max(fiveListB))

def average(lst):
    return round(sum(lst)/len(lst))
print(average(fiveListB))




