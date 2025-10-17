def first_setbit(number):
    count=1
    while(number):
        if (number & 1==1):
            break
        count+=1
        number>>1
    return count
number=int(input("Enter the number: "))
print("Position of the first set bit: ",first_setbit(number))