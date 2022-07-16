#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.rsalibnum import primes

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

def attack(n,e):
    for prime in primes(100000):
        if(n%prime==0):
            p=prime
            q=int(n/p)
            d=modinv(e,(p-1)*(q-1))
            return d

n=33
e=7
d = attack(n,e)
print(d)