import math
def printPowerSet(set,SetSize):
    #Find total elements possible in the power set
    PowerSetSize = int(math.pow(2,SetSize))
    outer = 0
    inner = 0
    for outer in range(0,PowerSetSize):
        for inner in range(0,SetSize):
            #Check if inner bit in the outer is set if set then print inner element from set
            if((outer & (1 << inner)) > 0):
                print(set[inner], end="  ")
        print("")
set=[]
n=str(input("Enter string : "))
for i in range (len(n)):
    set.append(n[i])
printPowerSet(set,len(set))