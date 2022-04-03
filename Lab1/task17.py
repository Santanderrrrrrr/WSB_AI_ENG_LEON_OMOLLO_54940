testNumber = int(input("Please enter the number for evenness test: "))

if testNumber>0:
    if ((testNumber%2) == 0 ):
        print("The number is an even number!")
    else:
        print("The number is odd")
else:
    print("enter a positive number")