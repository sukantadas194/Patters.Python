

#Print Custom Row-Column Patterns..
#e.g. '''@ @ @ @
#        @ @ @ @
#        @ @ @ @'''

w = print("What do you want to print?")
wa = str(input("Answer : "))
try:
    m1 = print("How many rows do you want to print?")
    n1 = int(input("Answer : "))
    m2 = print("How many columns do you want to print?")
    n2 = int(input("Answer : "))
    if n1 <= 0 or n2 <= 0:
        print("Wrong Input")
        print("Input should be positive & greater than '0'")
        print("Start over again..")

    for k in range(n1):
        for i in range(n2):
            print(wa, end=" ")
        print()
except:
    print("Wrong Input")
    print("Only numbers are accepted")
    print("Start over again..")