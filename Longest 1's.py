# Program to find the longest consecutive 1's in the binary representation of a number
# Take input from the user
number = int(input("Enter a number: "))
# Convert the number to binary
# bin() function returns a string like '0b1011', so we remove the first two characters
binary = bin(number)
print("Binary representation of", number, "is:", binary)
# Initialize variables
count = 0            # to count current consecutive 1's
max_count = 0        # to store the maximum consecutive 1's found so far
# Loop through each digit in the binary string
for bit in binary:
    if bit == '1':
        count += 1   # increase count if we find a '1'
        if count > max_count:
            max_count = count   # update max_count if needed
    else:
        count = 0    # reset count when we find a '0'
# Print the result
print("The longest consecutive 1's are:", max_count)