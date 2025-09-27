# number=int(input("Input number : "))
# result=0
# temp=number
# while temp!=0:
#     digit=temp%10
#     result=result+digit**3
#     temp=temp//10
# print(result)
# if number==result:
#     print(number," is an armstrong number ")
# else:
#     print(number," is not an armstrong number")
# #to find factors of user input
# def print_factors(number):
#     print("The factors of ",number," are:")
#     for i in range (1,number+1):
#         if number%i==0:
#             print(i)
# number=int(input("Enter your number to find its factors: "))
# print_factors(number)
def roman_to_int(a):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    int_form=0
    for i in range(len(a)):
        if i+1<len(a) and roman[a[i]]<roman[a[i+1]]:
            int_form-=roman[a[i]]
        else:
            int_form+=roman[a[i]]
    return int_form
a=input("Enter a roman numeral")
print(f"integer form of {a} is {roman_to_int(a)}")