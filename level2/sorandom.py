#!/usr/bin/python2

import sys, random

random.seed("random")
encflag = "BNZQ:6m3bd631074ov60jxu1zov1380l3i959"
cip = ''

for enc in encflag:
    if enc.islower():
        cip += chr((ord(enc)-ord('a') - random.randrange(0, 26))%26 + ord('a'))
    elif enc.isupper():
        cip += chr((ord(enc)-ord('A') - random.randrange(0, 26))%26 + ord('A'))
    elif enc.isdigit():
        cip += chr((ord(enc)-ord('0') - random.randrange(0, 10))%10 + ord('0'))
    else:
        cip += enc

print(cip)
