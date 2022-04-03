#Function max_sum(a, b, c) , which takes two largest numbers of the three
#given as arguments, sums these numbers and return their sum.

def max_sum(a, b, c):
    list = [ a, b, c]
    list.remove(min(list))
    return sum(list)
print(max_sum(4,2,3))


#Function return_even(x) , gets a list of numbers x and return a list of all the
#even numbers that were in x

def return_even(x):
    nuList = []
    for i in x:
        if (i%2==0):
            nuList.append(i)
    return nuList

y =[1,2,3,4,5,6,7,8,9]
print(return_even(y))


# Function trapezoid_area(a, b, h) , gets two basis of the trapezoid and the
# height of it. It computes and returns its area.

def trapezoid_area(a, b, h):
    return ((a+b)/2)*h

print (trapezoid_area(1,2,3))


# Function christmass(deco) gets a single character (e.g. a letter “o”) and prints
# a nice Christmas tree decorated with the given character deco.
def christmass(deco):
    print("    ^")
    print("   ^^^")
    print("  ^^",deco,"^")
    print(" ^^^",deco,"^^^^")
    print("  ^^^^^")
    print(" ^^",deco,"^^^^^")
    print("^^^^^^",deco,"^^^")
    print("   ###")

christmass("&")