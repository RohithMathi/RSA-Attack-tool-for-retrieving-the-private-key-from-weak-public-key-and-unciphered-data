#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from lib.rsalibnum import gcd, isqrt, next_prime, primes, powmod
from tqdm import tqdm

def pollard_P_1(n):
  z = []
  logn = math.log(int(isqrt(n)))
  prime = primes(997)

  for j in range(0, len(prime)):
      primej = prime[j]
      logp = math.log(primej)
      for i in range(1, int(logn / logp) + 1):
          z.append(primej)

      i = 0
      x = pp
      while 1:
        x = powmod(x, z[i], n)
        i = i + 1
        y = gcd(n, x - 1)
        if y != 1:
            p = y
            q = n // y
            return p, q
        if i >= len(z):
            return 0, None


from Crypto.PublicKey import RSA

key_data = """-----BEGIN PUBLIC KEY-----
MBswDQYJKoZIhvcNAQEBBQADCgAwBwICCg0CAQc=
-----END PUBLIC KEY-----"""
result = RSA.importKey(key_data)
p,q=pollard_P_1(result.n)
print(p*q==k.n)