def binary_to_decimal(binary,n):
    number=0
    for i in range(n):
        if binary[i]=='1':
            number=number+2**(n-(i+1))
        else:
            pass
    print(number)
binary=input("Enter your binary number: ")
n=len(binary)
binary_to_decimal(binary,n)