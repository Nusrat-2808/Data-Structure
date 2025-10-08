prime=[True for i in range(100+1)]
prime2digit=[]
p=2
while(p*p<=100):
    if (prime[p]==True):
        for i in range(p*p,100+1,p):
            prime[i]=False
    p+=1
for p in range(2,100+1):
    if prime[p]:
        prime2digit.append(p)
print(prime2digit)