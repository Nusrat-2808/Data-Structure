#Method 1(personal)
def prime(number):
    fact=[]
    for i in range(1,number+1):
        if number%i==0:
            fact.append(i)
        else:
            pass
    num=0
    for i in range(len(fact)):
        num+=1
    if num==2:
        print(f"The number({number}) is prime.")
    elif num==1:
        print(f"The number is neither prime nor consonant.")
    else:
        print(f"The number({number}) is consonant.")
number=int(input("Enter the number to check:  "))
prime(number)
#Method 2
number =int(input("Enter your number \n"))
if number>1:
    for i in range(2,number):
        if (number%i==0):
            print(number," is not prime.")
            break
        else:
            print(number, " is prime.")
else:
    print(number, " is not prime.")
#Seive of eratosthenes
def SeiveOfEratosthenes(num):
    prime=[True for i in range(num+1)]
    p=2
    while(p*p<=num):
        if (prime[p]==True):
            for i in range(p*p,num+1,p):
                prime[i]=False
        p+=1
    for p in range(2,num+1):
        if prime[p]:
            print(p)
num=int(input("Enter the number\n"))
print("Following are the prime numbers smaller")
print("than or equal to",num)
SeiveOfEratosthenes(num)