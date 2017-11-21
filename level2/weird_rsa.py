#!/usr/bin/python3

import sys
import binascii

# multiplicative inverse mod n
modinv = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or modinv(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

with open('weird_rsa.txt', 'r') as f:
    lines = f.read().splitlines()

# remove 'c: ' etc
rsa_vals = [i.split()[1] for i in lines]

c = int(rsa_vals[0])
p = int(rsa_vals[1])
q = int(rsa_vals[2])
dp = int(rsa_vals[3])
dq = int(rsa_vals[4])

q_inv = modinv(q, p)

m1 = pow(c, dp, p)
m2 = pow(c, dq, q)
h = (q_inv * (m1 - m2)) % p
m = m2 + h * q

msg = binascii.unhexlify(format(m, 'x')).decode()

print(msg)
