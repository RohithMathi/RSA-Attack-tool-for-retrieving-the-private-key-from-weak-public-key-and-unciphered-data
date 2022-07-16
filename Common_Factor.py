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

def attack(n1,n2,e1,e2):
    p=computeGCD(n1,n2)
    q1=int(n1/p)
    q2=int(n2/p)
    totient1=(p-1)*(q1-1)
    d1=modinv(e1,totient1)
    totient2=(p-1)*(q2-1)
    d2=modinv(e2,totient2)
    return d1,d2

n1=33
n2=77
e1=7
e2=7
d1,d2 = attack(n1,n2,e1,e2)
print(d1)
print(d2)