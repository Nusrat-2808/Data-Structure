def reverse_bits(n):
    # Find the number of bits needed to represent n
    num_bits = n.bit_length()
    
    # Initialize result
    reversed_num = 0
    
    for i in range(num_bits):
        # Shift reversed_num to the left
        reversed_num <<= 1
        # Add the least significant bit of n
        reversed_num |= (n & 1)
        # Shift n to the right
        n >>= 1
    
    return reversed_num

# Example usage
original = int(input("Enter your original number: "))
reversed_result = reverse_bits(original)
print("Reversed Number:", reversed_result)