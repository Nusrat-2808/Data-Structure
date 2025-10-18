# #Program to check if user input numbers are equal without using any comparison operator
# def checkIfSame(number1,number2):
#     #User XOR operator as a^a is always 0
#     if ((number1^number2) !=0):
#         print("Numbers are not equal.")
#     else:
#         print("Both numbers are equal")
# number1=int(input("Enter first number to compare: "))
# number2=int(input("Enter second number to compare: "))
# checkIfSame(number1,number2)
# #Program to find 1 OddOccuring number in array
# def OddOccuring(arr):
#     #Initialize result
#     res=0
#     #Traverse the array
#     for element in arr:
#         #XOR with the result
#         res=res^element
#     return res
# #Initialize our array
# arr=[]
# #Take array size as input
# n=int(input("Enter the array size : "))
# #Take array element as input
# while(n):
#     num=int(input("Enter number: "))
#     arr.append(num)
#     n-=1
# print("\n\n Odd occuring number is: ",OddOccuring(arr))
# #Program to find 2 odd occuring number in array
def printTwoOdd(arr,size):
    #XOR of 2 will hold Xor of the 2 odd occuring numbers
    xorof2=arr[0]
    #these will hold 2 odd occuring numbers
    x=0
    y=0
    #This will hold the rightmost set bit from Xor of 2
    Set_bit=0
    for i in range (1,size):
        xorof2=xorof2^arr[i]
    Set_bit=xorof2 & ~(xorof2-1)
    #if number is having set bit aat location we need then XOR it with x else y
    for i in range(size):
        if (arr[i] & Set_bit):
            x=x^arr[i]
        else:
            y=y^arr[i]
    print("Two odd elements are: ",x," & ",y)
arr=[]
arr_size=int(input("Enter the size of the array: "))
for i in range(0,arr_size):
    z=int(input("Enter element: "))
    arr.append(z)
printTwoOdd(arr,arr_size)