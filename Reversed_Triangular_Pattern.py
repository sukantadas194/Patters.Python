

#Print Reversed Triangle Patterns..
#e.g.   "@
#        @ @
#        @ @ @"

w = print("What do you want to print?")
wa = str(input("Answer : "))
try:
    m = print("How many rows do you want to print?")
    n = int(input("Answer : "))

    if n <= 0:
        print("Wrong Input")
        print("Input should be positive & greater than '0'")
        print("Start over again..")

    for k in range(n):
        for i in range(n-k):
            print(wa, end=" ")
        print()
except:
    print("Wrong Input")
    print("Only numbers are accepted")
    print("Start over again..")