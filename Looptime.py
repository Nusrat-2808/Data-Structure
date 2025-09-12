def myfunction(n):
    # --- First Loop ---
    for i in range(0, n+1):
        print("First Loop")
    print("Time Complexity of First Loop: O(n)")

    # --- Second Loop ---
    j = 1
    while (j <= n+1):
        print("Second Loop", j)
        j = j * 2
    print("Time Complexity of Second Loop: O(log n)")

    # --- Third Loop ---
    for i in range(0, 100):
        print("Third Loop")
    print("Time Complexity of Third Loop: O(1)")

    # --- Total ---
    print("Total Time Complexity: O(n)")


# --- Run the program ---
n = int(input("Enter value of n: "))
myfunction(n)
