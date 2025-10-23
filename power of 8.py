def powerof8(number):
    count=0
    #If only 1 set bit exists
    if ((number & (~(number-1)))==number):
        #Count 0 bits before set bit
        while(number>1):
            number>>=1
            count+=1
        #If count is even return true else false
        if (count%3==0):
            return True
        else:
            return False
number=int(input("Enter your number: "))
if (powerof8(number)):
    print(f"{number} is a power of 8")
else:
    print(f"{number} is not a power of 8")