def my_function():
    print("my function")
    print("I wrote something")
def functioning(a, b):
    S =a +b
    I = a*b
    D =a//b

    return[S, I, D]
my_function()
my_function()

wynik = functioning(10, 5)
print(wynik)
print(wynik[1])