#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def egcd(a, b):
    if (a == 0):
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m


print ('Small public Exponent')
g =12
e = 3
n = 1927
c= pow(g,e,n)
print('Cipher Text is :',c)
m = round(c**(1/3))
print ('Message recovered using small public Exponent is :',m,'\n\n\n')



print ('Hastads Attack')
g =17
e = 3

n1 = 1927
n2 = 187
n3 = 667

c1 = pow(g,e,n1)
c2 = pow(g,e,n2)
c3 = pow(g,e,n3)
print('Same Public Exponent used to Encrypt is : ',e)
print('Same Message Encrypted Cipher Text 1 is : ',c1)
print('Same Message Encrypted Cipher Text 2 is : ',c2)
print('Same Message Encrypted Cipher Text 3 is : ',c3)

N = n1*n2*n3
N1 = N//n1
N2 = N//n2
N3 = N//n3

u1 = modinv(N1,n1)
u2 = modinv(N2,n2)
u3 = modinv(N3,n3)

M = (c1*u1*N1 + c2*u2*N2 + c3*u3*N3) % N
m = round(M**(1/3))
print ('Message recovered using Hastads Attack is :',m)
