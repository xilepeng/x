def A(a, b):
    z = B(a,-b)
    return z

def B(a, b):
    z = C(a+ b)
    return z

def C(x):
    return x + 1
result = A(1, 2)
print( result )