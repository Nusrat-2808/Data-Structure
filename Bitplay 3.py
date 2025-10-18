#Program to swap two numbers without using third variable
def swap1(a,b):
    a = a ^ b
    b = a ^ b 
    a = a ^ b
    print(f"After swaping: a= {a} ; b= {b}")
def swap2(a,b):
    a=(a & b)+(a | b)
    b=a + (~b) +1
    a=a + (~b) +1
    print(f"After swaping: a= {a} ; b= {b}")
swap1(1,2)
swap2(1,2)
#Program to divide two numbers without using the division operator
def divide(ourdividend,ourdivisor):
    sign=(-1 if ((ourdividend < 0) ^ (ourdivisor < 0)) else 1)
    ourdividend=abs(ourdividend)
    ourdivisor=abs(ourdivisor)
    quotientNumber = 0
    tempNumber = 0
    for i in range(31,-1,-1):
        if (tempNumber + (ourdivisor<<i)<=ourdividend):
            tempNumber+=ourdivisor<<i
            quotientNumber |= 1 << i
    if sign==-1:
        quotientNumber= -quotientNumber
    return quotientNumber
a=int(input("Enter a for a/b: "))
b=int(input("Enter a for a/b: "))
print(f"Result of {a}/{b} is {divide(a,b)}")