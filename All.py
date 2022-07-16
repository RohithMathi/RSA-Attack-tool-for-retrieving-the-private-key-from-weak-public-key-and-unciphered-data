#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def isqrt(n):
    if n == 0:
        return 0
    x, y = n, (n + 1) >> 1
    while y < x:
        x, y = y, (y + n // y) >> 1
    return x

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
        raise ValueError("Modular inverse does not exist")
    else:
        return x % m



from factordb.factordb import FactorDB

def FactorDB_Attack(n,e):
	f = FactorDB(n)
	f.connect()
	result = f.get_factor_list()
	if(len(result) == 2):
	    p,q=result[0],result[1]
	    totient=(p-1)*(q-1)
	    d=modinv(e,totient)
	    return d,p,q
	else:
	    print("Not in DataBase")

n=1249110767794010895540410194153
e=65537
#d,p,q=FactorDB_Attack(n,e)
#print('FactorDB Ex private expoent:',d)



from lib.rsalibnum import primes

def Small_P_or_Q_Attack(n,e):
    for prime in primes(100000):
        if(n%prime==0):
            p=prime
            q=(n//p)
            d=modinv(e,(p-1)*(q-1))
            return d,p,q




def Fermat_Attack(n,e):
    if(n%2!=0):
        a = b = isqrt(n)
        b2 = pow(a, 2) - n
        while pow(b, 2) != b2:
            a += 1
            b2 = pow(a, 2) - n
            b = isqrt(b2)
        p, q = (a + b), (a - b)
        assert n == p * q
        if p is not None and q is not None:
            totient=(p-1)*(q-1)
            d=modinv(e,totient)
            return d,p,q
    else:
        totient=(2-1)*(n//2-1)
        d=modinv(e,totient)
        return d,2,n//2



def Common_Factor_Attack(n1,n2,e1,e2):
    p=computeGCD(n1,n2)
    if(p!=1):
        q1=(n1//p)
        q2=(n2//p)
        totient1=(p-1)*(q1-1)
        d1=modinv(e1,totient1)
        totient2=(p-1)*(q2-1)
        d2=modinv(e2,totient2)
        return d1,d2,p,q1,q2



def Common_Modulus_External_Attack(c1, c2, e1, e2, N):
    if computeGCD(e1, e2) != 1:
        raise ValueError("Exponents e1 and e2 must be coprime")
    s1 = modinv(e1,e2)
    s2 = ((computeGCD(e1,e2) - e1 * s1) // e2)
    temp = modinv(c2, N)
    m1 = pow(c1,s1,N)
    m2 = pow(temp,-1*s2,N)
    return (m1 * m2) % N



import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5

def Key_Reader(filename):
    x="/home/vishnu/project/examples/"+filename
    f = open(x, "r")
    key_data = f.read()
    result = RSA.importKey(key_data)
    return result




print('=========================================================')
k=Key_Reader("small_q.pub")
print('Public key of Small_P_or_Q\n')
pub_key = RSA.construct((k.n, k.e)).publickey().exportKey()
pub = RSA.importKey(pub_key)
print(pub_key.decode("utf-8"),'\n')

msg = input('Enter a message : ')
print("\nraw msg->", msg,'\n')
cipher = Cipher_PKCS1_v1_5.new(pub)
cipher_text = cipher.encrypt(msg.encode()) # now we have the cipher
print("cipher text->\n", cipher_text,'\n')

d,p,q = Small_P_or_Q_Attack(k.n,k.e)
print('Private key found using Small_P_or_Q_Attack\n')
priv_key = RSA.construct((k.n, k.e, d, p, q)).exportKey()
pri = RSA.importKey(priv_key)
print(priv_key.decode("utf-8"),'\n')

cipher = Cipher_PKCS1_v1_5.new(pri)
decrypt_text = cipher.decrypt(cipher_text, None).decode()
print("decrypted msg->", decrypt_text,'\n')
assert msg == decrypt_text # check that
print("Message Succesfully Decrypted")
print('=========================================================\n\n\n\n\n')




print('=========================================================')
k=Key_Reader("fermat.pub")
print('Public key of Fermat_Attack\n')
pub_key = RSA.construct((k.n, k.e)).publickey().exportKey()
pub = RSA.importKey(pub_key)
print(pub_key.decode("utf-8"),'\n')

msg = input('Enter a message : ')
print("\nraw msg->", msg,'\n')
cipher = Cipher_PKCS1_v1_5.new(pub)
cipher_text = cipher.encrypt(msg.encode()) # now we have the cipher
print("cipher text->\n", cipher_text,'\n')

d,p,q = Fermat_Attack(k.n,k.e)
print('Private key found using Fermat_Attack\n')
priv_key = RSA.construct((k.n, k.e, d, p, q)).exportKey()
pri = RSA.importKey(priv_key)
print(priv_key.decode("utf-8"),'\n')

cipher = Cipher_PKCS1_v1_5.new(pri)
decrypt_text = cipher.decrypt(cipher_text, None).decode()
print("decrypted msg->", decrypt_text,'\n')
assert msg == decrypt_text # check that
print("Message Succesfully Decrypted")
print('=========================================================\n\n\n\n\n')




print('=========================================================')
k1=Key_Reader("sharedp1.pem")
k2=Key_Reader("sharedp2.pem")
print('Public keys of Common_Factor_Attack\n')

pub_key1 = RSA.construct((k1.n, k1.e)).publickey().exportKey()
pub1 = RSA.importKey(pub_key1)
print(pub_key1.decode("utf-8"),'\n')

pub_key2 = RSA.construct((k2.n, k2.e)).publickey().exportKey()
pub2 = RSA.importKey(pub_key2)
print(pub_key2.decode("utf-8"),'\n')

msg = input('Enter a message : ')
print("\nraw msg->", msg,'\n')
cipher = Cipher_PKCS1_v1_5.new(pub1)
cipher_text = cipher.encrypt(msg.encode()) # now we have the cipher
print("cipher text->\n", cipher_text,'\n')

d1,d2,p,q1,q2 = Common_Factor_Attack(k1.n,k2.n,k1.e,k2.e)
print('Private keys found using Common_Factor_Attack\n')
priv_key1 = RSA.construct((k1.n, k1.e, d1, p, q1)).exportKey()
pri1 = RSA.importKey(priv_key1)
print(priv_key1.decode("utf-8"),'\n')

priv_key2 = RSA.construct((k2.n, k2.e, d2, p, q2)).exportKey()
pri2 = RSA.importKey(priv_key2)
print(priv_key2.decode("utf-8"),'\n')

cipher = Cipher_PKCS1_v1_5.new(pri1)
decrypt_text = cipher.decrypt(cipher_text, None).decode()
print("decrypted msg->", decrypt_text,'\n')
assert msg == decrypt_text # check that
print("Message Succesfully Decrypted")
print('=========================================================\n\n\n\n\n')






print('=========================================================')
print('Common_Modulus_Attack\n')
n = 19085995833312192524007220630153244389942263922006889142154298425751808612835625879164268530070480609
e1 = 31
e2 = 71
c1 = 6754157603566559210605055806173167464578011342930319568190139207096747909338872956835503565519657656
c2 = 15442865769085690326152463737212582797117727243803209188030346754687972404658825954014788039636105165
print('Common Modulus is : ',n)
print('Public Exponent 1 is : ',e1)
print('Public Exponent 2 is : ',e2)
print('Same Message Encrypted Cipher Text 1 is : ',c1)
print('Same Message Encrypted Cipher Text 2 is : ',c2)
retrieve_m=hex(Common_Modulus_External_Attack(c1,c2,e1,e2,n))
hex_string = retrieve_m[2:]
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print('\nRetrieved message is : ',ascii_string)
print('=========================================================')