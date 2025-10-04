#Activity 1
#Program to showcase working of different types of bitwise operators
num1=10
num2=4
#Using AND operator
print("num1 & num2 = ",num1 & num2)
#Using OR operator 
print("\n num1 | num2 = ", num1 | num2)
#Using NOT OPERATOR
print("\n ~num1 = ", ~num1)
# using XOR operator
print("\n num1 ^ num2 = ", num1 ^ num2)
#Using Right Shift operator on num1 and num2
print("\n num1 >> 1= ", num1 >> 1)
print("\n num2 >> 1 = ", num2 >> 1)
#Using Left Shift operator on num1 and num2
print("\n num1 << 1= ", num1 << 1)
print("\n num2 << 1 = ", num2 << 1)
#Activity 2
#Program to check if the user entered number is odd or even using only bitwise
#Returns true if n is even, else odd
def isEvenOdd(n):
    #XOR with 1 equals to n+1
    if (n^1 == n+1):
        return True
    else:
        return False
number= int(input("Enter your number : "))
if isEvenOdd(number):
    print(number," is Even")
else:
    print(number," is Odd")