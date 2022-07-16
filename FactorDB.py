#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from factordb.factordb import FactorDB

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

n=1249110767794010895540410194153
e=65537

f = FactorDB(n)
f.connect()
result = f.get_factor_list()
if(len(result) == 2):
    p,q=result[0],result[1]
    totient=(p-1)*(q-1)
    d=modinv(e,totient)
    print(d)
else:
    print("Not in DataBase")