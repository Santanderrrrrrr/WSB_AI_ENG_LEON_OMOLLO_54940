x= int(input("which number would you like to test?: "))

if x>1:
    for i in range(2, x//2):
        if((x%i)==0):
            print("The input number is not a prime number.")
    else:
        print("Yes, this is a prime number.")
elif x<0:
    print("Please enter a positive number.")
else:
    print("Zero is not a prime number.")
