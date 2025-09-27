#palindrome#take input from the user
number=int(input("Enter your number: "))
#Store the original number for comparison later
original_number=number
reversed_number=0
#Reverse the number
while number>0:
    digit=number%10
    reversed_number=reversed_number*10+digit
    number//=10
#Check if the original number & the reversed number are the same
if original_number==reversed_number:
    print(f"{original_number} is a palindrome.")
else: print(f"{original_number} is not a palindrome.")
#HCF
numberLargest=int(input("Enter the largest number: "))
numberSmallest=int(input("Enter the smallest number: "))
while numberSmallest:
    numberStore=numberSmallest
    numberSmallest=numberLargest%numberSmallest
    numberLargest=numberStore
print(f"HCF is : {numberLargest}")
#LCM
numberLargest=int(input("Enter the Largest number: "))
numberSmallest=int(input("Enter the Smallest number: "))
def LCM(a,b):
    product=a*b
    while b:
        numberStore=b
        b=a%b
        a=numberStore
    result=product/a
    print(result)
LCM(numberLargest,numberSmallest)