#Multiplying 2 numbers by 1 iteration function
def product1(M,N):
    print(M*N)
    print("Number of iteration is 1")
#Multiplying 2 numbers by N iteration function
def product2(M,N):
    result=0
    for _ in range(N):
        result+=M
    print(result)
    print(f"Number of iteration is {N}")
#Multiplying 2 numbers by (1+1+1...M times)+(1+1+1...M times)...N times iteration function
def product3(M,N):
    result=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            result+=1
    print(result)
    print(f"Number of iteration is {M*N}")
#Taking input of the numbers to be multiplied
M=int(input("Enter the 1st number: "))
N=int(input("Enter the 2nd number: "))
product1(M,N)
product2(M,N)
product3(M,N)