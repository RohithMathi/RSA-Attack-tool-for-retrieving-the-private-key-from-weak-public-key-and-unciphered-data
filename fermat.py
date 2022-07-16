#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def _isqrt(n):
    if n == 0:
        return 0
    x, y = n, (n + 1) >> 1
    while y < x:
        x, y = y, (y + n // y) >> 1
    return x

def fermat(n):
    a = b = _isqrt(n)
    b2 = pow(a, 2) - n
    while pow(b, 2) != b2:
        a += 1
        b2 = pow(a, 2) - n
        b = _isqrt(b2)
    p, q = (a + b), (a - b)
    assert n == p * q
    return p, q

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

def attack(n):
    p, q = fermat(n)
    if p is not None and q is not None:
        totient=(p-1)*(q-1)
        d=modinv(e,totient)
        return d

n=33
e=7
d = attack(n)
print(d)