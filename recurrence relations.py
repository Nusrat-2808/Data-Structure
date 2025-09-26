# Function 1: myfunction1
def myfunction1(n):
    if (n > 0):
        return
    # This loop runs n+1 times, so it's O(n)
    for i in range(0, n+1):
        print("Codingal")
    # Recursive calls with n/2 and n/3
    myfunction1(n / 2)
    myfunction1(n / 3)

# Function 2: myfunction2
def myfunction2(n):
    if (n <= 1):
        return
    # Constant time operation
    print("Codingal")
    # Recursive call with n-1
    myfunction2(n - 1)

# Print the recurrence relations
print("Recurrence for myfunction1: T(n) = T(n/2) + T(n/3) + O(n)")
print("Recurrence for myfunction2: T(n) = T(n-1) + O(1)")