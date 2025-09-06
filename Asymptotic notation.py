#O(1)Time
def printnumber(n):
    literation=0
    print("the total number entered by user is ",n)
    literation+=1
    print("total literation done by computer is",literation,"\n")
printnumber(10)
printnumber(200)
print("\n with any 'n' the time taken by the computer will not change.")
#O(n)Time
def OnTime(n):
    iteration=0
    for i in range (1,n+1):
        iteration+=1
    print("When n is ",n,"Iterations= ",iteration)
OnTime(10)
OnTime(20)
OnTime(42)
print("\nWith every 'n' the time taken and iteratrions will increase.")
#O(n^2)Time
def ONSquareTime(n):
    iteration=0
    for i in range (0,n):
        for j in range(0,n):
            print("*",end=" ")
            iteration+=1
        print("")
    print("\nWhen n is ",n,"Iterations= ",iteration,"\n")
ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)
print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")