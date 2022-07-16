#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def computeGCD(x, y):
   while(y):
       x, y = y, x % y
   return x

def egcd(a, b):
    if (a == 0):
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def attack(c1, c2, e1, e2, N):
    if computeGCD(e1, e2) != 1:
        raise ValueError("Exponents e1 and e2 must be coprime")
    s1 = modinv(e1,e2)
    s2 = int((computeGCD(e1,e2) - e1 * s1) / e2)
    temp = modinv(c2, N)
    m1 = pow(c1,s1,N)
    m2 = pow(temp,-1*s2,N)
    return (m1 * m2) % N

n=33
e1=3
e2=7
m=2
c1=pow(m,e1,n)
c2=pow(m,e2,n)
retrieve_m=attack(c1,c2,e1,e2,n)
print(retrieve_m)
