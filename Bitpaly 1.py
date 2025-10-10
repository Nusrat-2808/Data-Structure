#example
def firstSetBit(n):
    #Count variable set as 0
    count=1
    #Right shift the number till we find first set bit
    while(n):
        if (n&1==1):
            break
        count+=1
        n>>=1
    return count
print(firstSetBit(32))
#Activity 1
#Program to find the number of zero bits and one bits present in a number 
#Functions taking our number as input 
def numberofBits(n):
    ones=0
    zeros=0
    #while our number is greater than zero check last bit and right shift
    while(n):
        #use & operator to check if last bit is 1 or 0
        if (n&1==1):
            ones+=1
        else:
            zeros+=1
        #Right shift the number remove the last bit that we just checked above
        n>>=1
    print(f"\n\nOnes = {ones},\nZeros = {zeros}")
number=int(input("Enter your number : "))
numberofBits(number)
#activity 2
#program to check if the nth bit is set or not
def setOrnot(number,n):
    #make a mask variable by left shifting 1 (k-1) times and check if (n & mask ) equals to 1 or 0
    if number&(1 << n-1):
        print("\nSET")
    else:
        print("\nNOT SET")
number=int(input("Enter number: "))
n=int(input("Enter bit number: "))
setOrnot(number,n)