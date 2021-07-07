

#Print Custom Row-Column Patterns..
#e.g. '''# # # #
         # # # #
         # # # #'''
try:
    m1 = print("How many rows do you want to print?")
    n1 = int(input("Answer : "))
    m2 = print("How many columns do you want to print?")
    n2 = int(input("Answer : "))
    if n1 < 0 and n2 < 0:
        print("Wrong Input")
        print("Input should be a positive number")
        print("Start over again..")
    for k in range(n2):
        for i in range(n1):
            print("#", end=" ")
        print()
except:
    print("Wrong Input")
    print("Only numbers are accepted")
    print("Start over again..")