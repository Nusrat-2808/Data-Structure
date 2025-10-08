def circuit(A,B,C):
    d = A & B
    e = B | C
    f = B & C
    g = e & f
    Q = d | g
    print("Final output: ",Q)
circuit(0,1,1) 